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

def maxsum(arr):
    newlen = max(1,len(arr)/10)
    maxtmp = [0]*newlen
    for data in arr:
        for index in range(0,newlen):
            if data > maxtmp[index]:
                if index > 0:
                    maxtmp[index-1] = maxtmp[index]
                maxtmp[index] = data
            else:
                break
    return float(sum(maxtmp))/newlen  

def segsum(arr):
    arrlen = len(arr)
    tot = sum(arr)/arrlen
    seg = max(1,arrlen/10)
    ans = 0
    maxdis = 0
    nowsum = sum(arr[0:seg])
    for cnt in range(seg,arrlen-seg):
        nowsum += arr[seg]
        if abs((nowsum/(cnt+1) - tot)/(arrlen-(cnt+1))) > maxdis:
            maxdis = abs((nowsum/(cnt+1) - tot)/(arrlen-(cnt+1)))
            ans = cnt
    return sum(arr[0:ans+1])/(ans+1)

class recv_bit(gr.decim_block):
    """
    docstring for block recv_bit
    """
    def __init__(self, decim):
        gr.decim_block.__init__(self,
            name="recv_bit",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32,numpy.float32,numpy.float32], decim=decim)
        self.valuemax = 0
        self.valuemin = 0
        self.len = 0
        self.lenMax = 100
        self.decim = decim

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        minout = output_items[1]
        maxout = output_items[2]
        # <+signal processing here+>

        for i in range(0,len(in0)/self.decim):
            tot = float(sum(in0[i*self.decim:(i+1)*self.decim]))/self.decim
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
            out[i] = tot
            minout[i] = self.valuemin
            maxout[i] = self.valuemax
            if tot > (self.valuemax + self.valuemin)/2:
                self.valuemax = self.valuemax * 0.9 + tot * 0.1
            else:
                self.valuemin = self.valuemin * 0.9 + tot * 0.1
        #print('recv_bit: %f %f %f %f'%(in0[0],out[0],minout[0],maxout[0]))
        #print(len(out))
        return len(output_items[0])
