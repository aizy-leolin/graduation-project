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
import time
from gnuradio import gr

class find_preamble(gr.sync_block):
    """
    docstring for block find_preamble
    """
    def __init__(self, preamble,rate):
        gr.sync_block.__init__(self,
            name="find_preamble",
            in_sig=[numpy.byte],
            out_sig=[numpy.byte])
        self.preamble = preamble
        self.rate = rate
        self.preamble_len = len(preamble)
        self.state = False
        self.cache = [0]*self.preamble_len
        self.now = 0
        self.cnt = 0 
        self.truecnt = 0
        #self.file = open('/home/huangxf/preamblecnt.txt','w')



    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        tmp = time.time()
        for x in range(len(in0)):
            
            if self.state:
                out[x] = 1
                self.state=False
            else:
                out[x] = 0

            self.cache[self.now] = in0[x]
            self.cnt += 1
            if self.cnt < self.preamble_len:               
                self.now += 1
                continue
            wrong = 0
            for data in self.preamble:
                self.now += 1
                if self.now == self.preamble_len:
                    self.now = 0
                if self.cache[self.now] == data:
                    continue
                wrong += 1
            if wrong * self.rate < self.preamble_len:
                self.state = True
                self.truecnt += 1
                print('%d %d \n'%(self.truecnt,self.cnt))
            self.now += 1
            if self.now == self.preamble_len:
                self.now = 0 

        print('find_preamble: %f'%((time.time()-tmp)/len(input_items[0])))
        return len(output_items[0])

