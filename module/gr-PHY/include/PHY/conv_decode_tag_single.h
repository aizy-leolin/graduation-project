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


#ifndef INCLUDED_PHY_CONV_DECODE_TAG_SINGLE_H
#define INCLUDED_PHY_CONV_DECODE_TAG_SINGLE_H

#include <PHY/api.h>
#include <gnuradio/tagged_stream_block.h>

namespace gr {
  namespace PHY {

    /*!
     * \brief <+description of block+>
     * \ingroup PHY
     *
     */
    class PHY_API conv_decode_tag_single : virtual public gr::tagged_stream_block
    {
     public:
      typedef boost::shared_ptr<conv_decode_tag_single> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of PHY::conv_decode_tag_single.
       *
       * To avoid accidental use of raw pointers, PHY::conv_decode_tag_single's
       * constructor is in a private implementation
       * class. PHY::conv_decode_tag_single::make is the public interface for
       * creating new instances.
       */
      static sptr make(const std::string& lengthtagname="packet_len");
    };

  } // namespace PHY
} // namespace gr

#endif /* INCLUDED_PHY_CONV_DECODE_TAG_SINGLE_H */

