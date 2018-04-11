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


#ifndef INCLUDED_PHY_WAVE_TO_FLOAT_SINGLE_CPP_H
#define INCLUDED_PHY_WAVE_TO_FLOAT_SINGLE_CPP_H

#include <PHY/api.h>
#include <gnuradio/sync_decimator.h>

namespace gr {
  namespace PHY {

    /*!
     * \brief <+description of block+>
     * \ingroup PHY
     *
     */
    class PHY_API wave_to_float_single_cpp : virtual public gr::sync_decimator
    {
     public:
      typedef boost::shared_ptr<wave_to_float_single_cpp> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of PHY::wave_to_float_single_cpp.
       *
       * To avoid accidental use of raw pointers, PHY::wave_to_float_single_cpp's
       * constructor is in a private implementation
       * class. PHY::wave_to_float_single_cpp::make is the public interface for
       * creating new instances.
       */
      static sptr make(int decim);
    };

  } // namespace PHY
} // namespace gr

#endif /* INCLUDED_PHY_WAVE_TO_FLOAT_SINGLE_CPP_H */

