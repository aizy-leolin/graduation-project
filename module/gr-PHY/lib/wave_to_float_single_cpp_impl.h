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

#ifndef INCLUDED_PHY_WAVE_TO_FLOAT_SINGLE_CPP_IMPL_H
#define INCLUDED_PHY_WAVE_TO_FLOAT_SINGLE_CPP_IMPL_H

#include <PHY/wave_to_float_single_cpp.h>

namespace gr {
  namespace PHY {

    class wave_to_float_single_cpp_impl : public wave_to_float_single_cpp
    {
     private:
      // Nothing to declare in this block.

     public:
      wave_to_float_single_cpp_impl(int decim);
      ~wave_to_float_single_cpp_impl();

      int decim,maxlen,len;
      float valuemin,valuemax;
      bool state;
      float *cache;
      float maxsplitdis;
      int maxsplitpos;

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
      float maxsplit(const float *in);
      float abs(float x);
    };

  } // namespace PHY
} // namespace gr

#endif /* INCLUDED_PHY_WAVE_TO_FLOAT_SINGLE_CPP_IMPL_H */

