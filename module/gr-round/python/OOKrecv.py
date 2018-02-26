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

class OOKrecv(gr.decim_block):
    """
    docstring for block OOKrecv
    """
    def __init__(self, deci,value):
        gr.decim_block.__init__(self,
            name="OOKrecv",
            in_sig=[numpy.float32],
            out_sig=[numpy.byte], decim=deci)
        self.deci = deci
        self.valuemax = float(value)
        self.valuemin = 0
        self.file=open('/home/huangxf/test/temp.txt','w')
        self.file2=open('/home/huangxf/test/temp2.txt','w')

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        print(in0.shape)
        print(self.valuemax)
        print(self.valuemin)
        for i in range(0,len(in0)/self.deci):
            tot = float(sum(in0[i*self.deci:(i+1)*self.deci]))/self.deci
            if tot>(self.valuemax+self.valuemin)/2:
                out[i] = 1
                self.valuemax = (self.valuemax*0.9 + tot*0.1)
            else:
                out[i] = 0
                self.valuemin = (self.valuemin*0.9 + tot*0.1)
            self.file.write(str(out[i])+'\n')
            for x in range(0,10):
                self.file2.write(str(in0[i*self.deci+x*self.deci/100])+'\n')
        #out[:] = in0
        return len(output_items[0])

