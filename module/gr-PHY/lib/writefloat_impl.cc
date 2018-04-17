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
#include "writefloat_impl.h"

namespace gr {
  namespace PHY {

    writefloat::sptr
    writefloat::make()
    {
      return gnuradio::get_initial_sptr
        (new writefloat_impl());
    }

    /*
     * The private constructor
     */
    writefloat_impl::writefloat_impl()
      : gr::sync_block("writefloat",
              gr::io_signature::make(1,1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)))
    {
    	file.open("SNR.txt");
    }

    /*
     * Our virtual destructor.
     */
    writefloat_impl::~writefloat_impl()
    {
    }

    int
    writefloat_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];


      for (int i=0;i<noutput_items;++i)
      {
      	file<<*(in)<<std::endl;
      	*(out++) = *(in++);
      }
      // Do <+signal processing+>

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace PHY */
} /* namespace gr */

