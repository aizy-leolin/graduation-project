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

class float_to_bit(gr.sync_block):
    """
    docstring for block float_to_bit
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="float_to_bit",
            in_sig=[numpy.float32,numpy.float32,numpy.float32],
            out_sig=[numpy.byte])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        minin = input_items[1]
        maxin = input_items[2]
        out = output_items[0]
        # <+signal processing here+>
        for x in range(len(in0)):
            if in0[x] > (maxin[x] * 0.3 + minin[0] * 0.7):
                out[x] = 1
            else:
                out[x] = 0
        return len(output_items[0])

