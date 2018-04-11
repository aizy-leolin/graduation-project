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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "float_to_bit_cpp_impl.h"
//#include <ctime>
namespace gr {
  namespace PHY {

    float_to_bit_cpp::sptr
    float_to_bit_cpp::make()
    {
      return gnuradio::get_initial_sptr
        (new float_to_bit_cpp_impl());
    }

    /*
     * The private constructor
     */
    float_to_bit_cpp_impl::float_to_bit_cpp_impl()
      : gr::sync_block("float_to_bit_cpp",
              gr::io_signature::make(3, 3, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(unsigned char)))
    {}

    /*
     * Our virtual destructor.
     */
    float_to_bit_cpp_impl::~float_to_bit_cpp_impl()
    {
    }

    int
    float_to_bit_cpp_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const  float *in = (const float *) input_items[0];
      const  float *minin = (const float *) input_items[1];
      const  float *maxin = (const float *) input_items[2];
      unsigned char *out = (unsigned char *) output_items[0];

      // Do <+signal processing+>
      //clock_t start = clock();
      for (int i=0; i<noutput_items; ++i)
      {
        if (in[i] > (maxin[i]*0.3 + minin[i]*0.7))
          out[i] = 1;
        else
          out[i] = 0;
      }
      //printf("float_to_bit_cpp: %.10f\n",(double(clock()-start)/CLOCKS_PER_SEC)/noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace PHY */
} /* namespace gr */

