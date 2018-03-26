/* -*- c++ -*- */
/* 
 * Copyright 2018 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_PHY_CONV_DECODE_TAG_IMPL_H
#define INCLUDED_PHY_CONV_DECODE_TAG_IMPL_H

#include <PHY/conv_decode_tag.h>
#include <fstream>
namespace gr {
  namespace PHY {

    class conv_decode_tag_impl : public conv_decode_tag
    {
     private:
      // Nothing to declare in this block.

     protected:
      int calculate_output_stream_length(const gr_vector_int &ninput_items);

     public:
      conv_decode_tag_impl(const std::string &lengthtagname);
      ~conv_decode_tag_impl();

      // Where all the action really happens
      int work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
      std::string lengthtag;

      int g0,g1;
      int state;
      int encode0[1<<7],encode1[1<<7];
      //std::ofstream file;
    };

  } // namespace PHY
} // namespace gr

#endif /* INCLUDED_PHY_CONV_DECODE_TAG_IMPL_H */

