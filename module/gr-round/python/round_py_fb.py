#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
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

class round_py_fb(gr.sync_block):
    """
    docstring for block round_py_fb
    """
    def __init__(self,test):
        gr.sync_block.__init__(self,
            name="round_py_fb",
            in_sig=[numpy.float32],
            out_sig=[numpy.uint8])
        self.test = test
        self.file=open('/home/huangxf/test/temp.txt','w')
        self.file2=open('/home/huangxf/test/temp2.txt','w')
        self.cnt=0


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = numpy.where(in0>self.test,1,0)
        print(out.shape)
        #print(out[:])
        for x in out[:]:
            #print(x)
            self.file.write(str(x)+'\n')
        for x in in0[:]:
            self.file2.write(str(x)+'\n')
        return len(output_items[0])

