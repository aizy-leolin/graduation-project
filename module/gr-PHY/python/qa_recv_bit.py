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
from recv_bit import recv_bit

class qa_recv_bit (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        self.tb.run ()
        # check data


    def test_001_recv_bit(self):

    	src_data = [0,0.1,1.2,0.8,0.3,0.1,0.9,1.1,0.5,0.2]
    	expected_result = (0,0,0,0,0)
    	src = blocks.vector_source_f(src_data)
    	dec = recv_bit(2)
    	snk = blocks.vector_sink_f()
        snk2 = blocks.vector_sink_f()
        snk3 = blocks.vector_sink_f()
    	self.tb.connect(src,(dec,0),snk)
        self.tb.connect((dec,1),snk2)
        self.tb.connect((dec,2),snk3)
    	self.tb.run()

    	result_data = snk.data()
    	self.assertAlmostEqual(result_data,expected_result)



if __name__ == '__main__':
    gr_unittest.run(qa_recv_bit, "qa_recv_bit.xml")
