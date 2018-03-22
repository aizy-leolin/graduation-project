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
from find_preamble import find_preamble

class qa_find_preamble (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        self.tb.run ()
        # check data

    def test_001_find_preamble(self):

    	src_data = [1,0,0,1,0,1,1,1,0,0,1,0,0]
    	expected_result = (0,0,0,0,1,0,0,0,0,0,0,1,0)
    	src = blocks.vector_source_b(src_data)
    	preamble = (1,0,0,1)
    	find = find_preamble(preamble,30)
    	snk = blocks.vector_sink_b()
    	self.tb.connect(src,find,snk)
    	self.tb.run()

    	result_data = snk.data()
    	self.assertEqual(result_data,expected_result)


if __name__ == '__main__':
    gr_unittest.run(qa_find_preamble, "qa_find_preamble.xml")
