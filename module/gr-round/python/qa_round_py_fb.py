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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from round_py_fb import round_py_fb
import numpy as np

class qa_round_py_fb (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        self.tb.run ()
        # check data

    def test_001_round(self):
    	src_data = np.random.rand(100000,)
    	expected_data = tuple(np.where(src_data>0.5,1,0))
    	src = blocks.vector_source_f(src_data)
    	rod = round_py_fb(0.5)
    	snk = blocks.vector_sink_b()
    	self.tb.connect(src,rod,snk)
    	self.tb.run()
    	result_data = snk.data()
    	self.assertTupleEqual(expected_data,result_data,100000)


if __name__ == '__main__':
    gr_unittest.run(qa_round_py_fb, "qa_round_py_fb.xml")
