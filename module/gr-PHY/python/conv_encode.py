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

class conv_encode(gr.interp_block):
    """
    docstring for block conv_encode
    """
    def __init__(self):
        gr.interp_block.__init__(self,
            name="conv_encode",
            in_sig=[numpy.byte],
            out_sig=[numpy.float32], interp=2)
        self.history = 0


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        #print(len(in0))
        #print(len(out))
        # <+signal processing here+>
        for i in range(0,len(in0)):
            #print(i)
            out[i<<1] = (in0[i]&1) ^ (self.history & 1) ^ ((self.history >> 1) & 1) ^ ((self.history >> 3 ) & 1) ^ ((self.history >> 4) & 1) 
            #print(i<<1+1)
            out[(i<<1) + 1] = (in0[i]&1) ^ (self.history & 1) ^ ((self.history >> 3) & 1) ^ ((self.history >> 4) & 1) ^ ((self.history >> 5) & 1) 
            self.history = (self.history >> 1) + ((in0[i]&1) << 5 )

        return len(output_items[0])

