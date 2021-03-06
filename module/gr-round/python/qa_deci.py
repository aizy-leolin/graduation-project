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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from deci import deci
import numpy as np

class qa_deci (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        self.tb.run ()
        # check data

    def test_001_deci(self):
    	src_data = np.random.rand(10000,)
    	src = blocks.vector_source_f(src_data)
    	dec = deci(1000)
    	snk = blocks.vector_sink_f()
    	self.tb.connect(src,dec,snk)
    	self.tb.run()

    	result_data = snk.data()

    	self.assertAlmostEqual(result_data[0],src_data[0])
    	self.assertAlmostEqual(result_data[1],src_data[1000])
    	self.assertAlmostEqual(result_data[2],src_data[2000])
    	self.assertAlmostEqual(result_data[3],src_data[3000])


if __name__ == '__main__':
    gr_unittest.run(qa_deci, "qa_deci.xml")
