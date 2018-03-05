#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class conv_decode(gr.decim_block):
    """
    docstring for block conv_decode
    """
    def __init__(self, window):
        gr.decim_block.__init__(self,
            name="conv_decode",
            in_sig=[numpy.float32,numpy.float32,numpy.float32],
            out_sig=[numpy.byte], decim=2)
        self.window = window
        self.state = 64
        self.route = numpy.zeros((window,self.state),dtype=numpy.int32)
        self.likehood = numpy.zeros((self.state))
        self.oldlikehood = numpy.zeros((self.state))
        
        self.received = 0
        self.now = 0
        self.file=open('/home/huangxf/test/temp.txt','w')
        self.file2=open('/home/huangxf/test/temp2.txt','w')

        # get state encode output prepared
        self.g0 = 0133
        self.g1 = 0171
        self.encode0 = numpy.zeros((self.state<<1),dtype=numpy.int32)
        self.encode1 = numpy.zeros((self.state<<1),dtype=numpy.int32)
        for i in range(self.state<<1):
            tmp = i & self.g0
            self.encode0[i] = (tmp & 1) ^ ((tmp >> 1) & 1 ) ^ ((tmp >> 2) & 1 ) ^ ((tmp >> 3) & 1 ) ^ ((tmp >> 4) & 1 ) ^ ((tmp >> 5) & 1 ) ^ ((tmp >> 6) & 1 )
            tmp = i & self.g1
            self.encode1[i] = (tmp & 1) ^ ((tmp >> 1) & 1 ) ^ ((tmp >> 2) & 1 ) ^ ((tmp >> 3) & 1 ) ^ ((tmp >> 4) & 1 ) ^ ((tmp >> 5) & 1 ) ^ ((tmp >> 6) & 1 )

    def work(self, input_items, output_items):
        in0 = input_items[0]
        minin = input_items[1]
        maxin = input_items[2]
        out = output_items[0]
        x = 0
        y = 0
        z = 0
        likehood1 = 0
        likehood2 = 0
        beststate = 0
        # <+signal processing here+>

        for i in range(0,len(in0)/2):
            bestlikehood = 1000000000
            std0 = [minin[i<<1],maxin[i<<1]]
            std1 = [minin[(i<<1)+1],maxin[(i<<1)+1]]
            for j in range(0,self.state):

                x = (j & 0x1F) <<1
                y = ((j & 0x1F) <<1 ) +1
                if ((j>>5) == 0):

                    likehood2 = self.oldlikehood[y] + abs(in0[i<<1]-std0[self.encode0[y]]) + abs(in0[(i<<1)+1]-std1[self.encode1[y]])
                    likehood1 = self.oldlikehood[x] + abs(in0[i<<1]-std0[self.encode0[x]]) + abs(in0[(i<<1)+1]-std1[self.encode1[x]])
                    if likehood1 > likehood2:
                        self.route[self.now,j] = y 
                        self.likehood[j] = likehood2
                    else:
                        self.route[self.now,j] = x 
                        self.likehood[j] = likehood1

                else:
                    likehood2 = self.oldlikehood[y] + abs(in0[i<<1]-std0[self.encode0[y|0x40]]) + abs(in0[(i<<1)+1]-std1[self.encode1[y|0x40]])
                    likehood1 = self.oldlikehood[x] + abs(in0[i<<1]-std0[self.encode0[x|0x40]]) + abs(in0[(i<<1)+1]-std1[self.encode1[x|0x40]])
                    if likehood1 > likehood2:
                        self.route[self.now,j] = y 
                        self.likehood[j] = likehood2
                    else:
                        self.route[self.now,j] = x 
                        self.likehood[j] = likehood1
                if self.likehood[j] < bestlikehood:
                    bestlikehood = self.likehood[j]
                    beststate = j

            self.oldlikehood = self.likehood.copy()
            if self.received < self.window:
                self.received += 1
                out[i] = 0
                self.now += 1
                if self.now == self.window:
                    self.now = 0
                continue
            level = self.now
            for j in range(0,self.window):
                beststate = self.route[level,beststate]
                level -= 1
                if level < 0:
                    level += self.window
            out[i] = beststate >> 5
            self.file.write(str(out[i])+'\n')
            self.file2.write(str(in0[i<<1])+' '+str(in0[(i<<1)+1])+'\n')
            self.now += 1
            if self.now == self.window:
                self.now = 0
        print(minin[0])
        print(maxin[0])

        return len(output_items[0])

