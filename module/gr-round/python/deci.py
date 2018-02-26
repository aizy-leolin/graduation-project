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

class deci(gr.decim_block):
    """
    docstring for block deci
    """
    def __init__(self, deci=2000):
        gr.decim_block.__init__(self,
            name="deci",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32], decim=deci)
        self.decim = deci

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        print(len(in0))
        for i in range(0,len(in0)/self.decim):
            out[i] = in0[i*self.decim]
        #out[:] = in0
        return len(output_items[0])

