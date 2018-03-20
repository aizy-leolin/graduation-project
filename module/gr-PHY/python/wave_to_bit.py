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



class wave_to_bit(gr.decim_block):
    """
    docstring for block wave_to_bit
    """
    def __init__(self, decim):
        gr.decim_block.__init__(self,
            name="recv_bit",
            in_sig=[numpy.float32],
            out_sig=[numpy.byte], decim=decim)
        self.valuemax = 0
        self.valuemin = 0
        self.len = 0
        self.lenMax = 100
        self.decim = decim
        self.file=open('/home/huangxf/test/temp3.txt','w')
        
        self.interval = self.decim/10
        self.cache=numpy.zeros(self.interval)
        

    def bit_sync(self,arr):
        maxdis = abs(sum(self.cache)/len(self.cache)*self.interval - sum(arr[0:self.interval]))
        pos = -1
        for x in range(9):
            dis = abs(sum(arr[x*self.interval:(x+1)*self.interval])-sum(arr[(x+1)*self.interval:(x+2)*self.interval]))
            if maxdis < dis:
                maxdis = dis
                pos = x
        if pos < 0:
            self.cache = arr[self.interval*9:].copy()
            return sum(arr)/self.decim
        else:
            ans = (sum(self.cache)+sum(arr[0:(pos+1)*self.interval]))/(len(self.cache)+(pos+1)*self.interval)
            self.cache = arr[self.interval*(pos+1):].copy()
            return ans

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>

        for i in range(0,len(in0)/self.decim):
            if self.decim < 10:
                tot = float(sum(in0[i*self.decim:(i+1)*self.decim]))/self.decim
            else:
                tot = self.bit_sync(in0[i*self.decim:(i+1)*self.decim])
            #tot = maxsum(in0[i*self.decim:(i+1)*self.decim])
            #tot = segsum(in0[i*self.decim:(i+1)*self.decim])
            if self.len < self.lenMax:
                if self.len == 0:
                    self.valuemin = tot
                    self.valuemax = tot
                    self.len += 1
                    continue 
                self.len += 1
                #print('len: %d'%self.len)
                if tot > self.valuemax:
                    self.valuemax = self.valuemax*0.2 + tot*0.8
                if tot < self.valuemin:
                    self.valuemin = self.valuemin * 0.5 + tot * 0.5
                continue
            if tot > (self.valuemax + self.valuemin)/2:
                self.valuemax = self.valuemax * 0.9 + tot * 0.1
                out[i]=1
            else:
                self.valuemin = self.valuemin * 0.9 + tot * 0.1
                out[i]=0
        self.file.write(str(in0[-1])+' '+str(out[-1])+' '+str(self.valuemin)+' '+str(self.valuemax)+'\n')
        #print('recv_bit: %f %f %f %f'%(in0[0],out[0],minout[0],maxout[0]))
        #print(len(out))
        return len(output_items[0])
