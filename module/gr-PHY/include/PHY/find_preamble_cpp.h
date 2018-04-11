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


#ifndef INCLUDED_PHY_FIND_PREAMBLE_CPP_H
#define INCLUDED_PHY_FIND_PREAMBLE_CPP_H

#include <PHY/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace PHY {

    /*!
     * \brief <+description of block+>
     * \ingroup PHY
     *
     */
    class PHY_API find_preamble_cpp : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<find_preamble_cpp> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of PHY::find_preamble_cpp.
       *
       * To avoid accidental use of raw pointers, PHY::find_preamble_cpp's
       * constructor is in a private implementation
       * class. PHY::find_preamble_cpp::make is the public interface for
       * creating new instances.
       */
      static sptr make(const std::vector<int> &preamble,int rate,int skip);
    };

  } // namespace PHY
} // namespace gr

#endif /* INCLUDED_PHY_FIND_PREAMBLE_CPP_H */

