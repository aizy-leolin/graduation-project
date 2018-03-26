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
#include "conv_encode_tag_impl.h"

namespace gr {
  namespace PHY {

    conv_encode_tag::sptr
    conv_encode_tag::make(const std::string &lengthtagname)
    {
      return gnuradio::get_initial_sptr
        (new conv_encode_tag_impl(lengthtagname));
    }

    /*
     * The private constructor
     */
    conv_encode_tag_impl::conv_encode_tag_impl(const std::string &lengthtagname)
      : gr::tagged_stream_block("conv_encode_tag",
              gr::io_signature::make(1, 1, sizeof(char)),
              gr::io_signature::make(1, 1, sizeof(char)), lengthtagname),lengthtag(lengthtagname)
    {
   		//this->file.open("test.txt",std::ios::out);   
    	set_tag_propagation_policy(TPP_DONT);
    }

    /*
     * Our virtual destructor.
     */
    conv_encode_tag_impl::~conv_encode_tag_impl()
    {
    }

    int
    conv_encode_tag_impl::calculate_output_stream_length(const gr_vector_int &ninput_items)
    {
      //int noutput_items = ( ninput_items[0] + 6 )<<1 ;
      //this->file<<"outputlen: "<<( ninput_items[0] + 6 )*2<<std::endl;
      return ( ninput_items[0] + 6 )*2 ;
    }

    int
    conv_encode_tag_impl::work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      //this->file<<"noutput_items: "<<noutput_items<<std::endl;
      const unsigned char *in = (const unsigned char *) input_items[0];
      unsigned char *out = (unsigned char *) output_items[0];

      unsigned char history = 0;
      
      for (int i=0; i < ninput_items[0];++i)
      {
      	*(out++) = ((*in)&1) ^ (history&1) ^ ((history>>1)&1) ^ ((history>>3)&1) ^ ((history>>4)&1);
      	*(out++) = ((*in)&1) ^ (history&1) ^ ((history>>3)&1) ^ ((history>>4)&1) ^ ((history>>5)&1);
      	history = (history>>1) + (((*in)&1)<<5);
      	++in;
      }

      for (int i = ninput_items[0]; i < ninput_items[0]+6; ++i)
      {
      	*(out++) = (history&1) ^ ((history>>1)&1) ^ ((history>>3)&1) ^ ((history>>4)&1);
      	*(out++) = (history&1) ^ ((history>>3)&1) ^ ((history>>4)&1) ^ ((history>>5)&1);
      	history = (history>>1);
      }
      
      std::vector <tag_t> tags;
      get_tags_in_range(tags,0,nitems_read(0),nitems_read(0)+ninput_items[0]);
      //this->file<<tags.size()<<std::endl;
      //this->file<<"input size:"<<nitems_read(0)<<"  "<<nitems_written(0)<<"  "<<ninput_items[0]<<"  "<<noutput_items<<std::endl;
      for (size_t i=0; i<tags.size(); ++i)
      {
      	tags[i].offset -= nitems_read(0);
      	//this->file<<int(tags[i].offset)<<std::endl;
      	add_item_tag(0,nitems_written(0) + ((tags[i].offset+6)<<1),tags[i].key,tags[i].value);
      }
      //add_item_tag(0,nitems_written(0) + ((ninput_items[0]+6)<<1),pmt::string_to_symbol(this->lengthtag),pmt::from_long(((ninput_items[0]+6)<<1)));
      //this->file.close();
      // Do <+signal processing+>

      // Tell runtime system how many output items we produced.
      //return noutput_items;
      return (ninput_items[0]+6)<<1;
    }

  } /* namespace PHY */
} /* namespace gr */

