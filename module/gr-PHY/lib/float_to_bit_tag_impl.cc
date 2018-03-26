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
#include "float_to_bit_tag_impl.h"

namespace gr {
  namespace PHY {

    float_to_bit_tag::sptr
    float_to_bit_tag::make(const std::string &lengthtagname)
    {
      return gnuradio::get_initial_sptr
        (new float_to_bit_tag_impl(lengthtagname));
    }

    /*
     * The private constructor
     */
    float_to_bit_tag_impl::float_to_bit_tag_impl(const std::string &lengthtagname)
      : gr::tagged_stream_block("float_to_bit_tag",
              gr::io_signature::make(3, 3, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(unsigned char)), lengthtagname)
    {
      set_tag_propagation_policy(TPP_DONT);
    }

    /*
     * Our virtual destructor.
     */
    float_to_bit_tag_impl::~float_to_bit_tag_impl()
    {
    }

    int
    float_to_bit_tag_impl::calculate_output_stream_length(const gr_vector_int &ninput_items)
    {
      int noutput_items = ninput_items[0];
      return noutput_items ;
    }

    int
    float_to_bit_tag_impl::work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      //printf("%d %d %d\n",int(ninput_items[0]),int(ninput_items[1]),int(ninput_items[2]) );
      const float *in = (const float *) input_items[0];
      const float *minin = (const float *) input_items[1];
      const float *maxin = (const float *) input_items[2];
      unsigned char *out = (unsigned char *) output_items[0];
      for (int i = 0; i < ninput_items[0]; ++i)
      {
        if (*(in++)> *(maxin++) * 0.3 + *(minin++) * 0.7)
          *(out++)=1;
        else
          *(out++)=0;
      }
      
      std::vector<tag_t> tags;
      get_tags_in_range(tags,0,nitems_read(0),nitems_read(0)+ninput_items[0]);
      for (int i = 0; i<tags.size(); ++i)
      {
        tags[i].offset -= nitems_read(0);
        add_item_tag(0,tags[i].offset,tags[i].key,tags[i].value);
      }

      // Do <+signal processing+>

      // Tell runtime system how many output items we produced.
      return ninput_items[0];
    }

  } /* namespace PHY */
} /* namespace gr */

