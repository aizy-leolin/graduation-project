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
#include "find_preamble_cpp_impl.h"
//#include <ctime>
namespace gr {
  namespace PHY {

    find_preamble_cpp::sptr
    find_preamble_cpp::make(const std::vector<int> &preamble,int rate,int skip)
    {
      return gnuradio::get_initial_sptr
        (new find_preamble_cpp_impl(preamble, rate, skip));
    }

    /*
     * The private constructor
     */
    find_preamble_cpp_impl::find_preamble_cpp_impl(const std::vector<int> &preamble, int rate, int skip)
      : gr::sync_block("find_preamble_cpp",
              gr::io_signature::make(1, 1, sizeof(unsigned char)),
              gr::io_signature::make(1, 1, sizeof(unsigned char))),preamble(preamble),rate(rate),skip(skip)
    {
      this->state = 0;
      this->cache = new int[this->preamble.size()];
      this->preamblelen = this->preamble.size();
      this->now = 0;
      this->cnt = 0;
      this->truecnt = 0;
    }

    /*
     * Our virtual destructor.
     */
    find_preamble_cpp_impl::~find_preamble_cpp_impl()
    {
    }

    int
    find_preamble_cpp_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const unsigned char *in = (const unsigned char *) input_items[0];
      unsigned char *out = (unsigned char *) output_items[0];
      //clock_t start = clock();
      // Do <+signal processing+>
      int wrong;
      bool flag=false;
      for (int i=0; i<noutput_items; ++i)
      {


        this->cache[this->now] = in[i];
        ++this->cnt;
        if (this->cnt < this->preamble.size())
        {
          ++this->now;
          continue;
        }

        if (this->state)
        {
          if (this->state==this->skip) {out[i] = 1;flag=true;++this->truecnt;printf("truecnt: %d totcnt: %d\n",this->truecnt,this->cnt);}
          else out[i]=0;
          --this->state;
          continue;
        }
        else out[i] = 0;

        wrong = 0;
        for (int j=0; j<this->preamblelen; ++j)
        {
          ++this->now;
          if (this->now == this->preamblelen) this->now = 0;
          if (this->cache[this->now] == this->preamble[j]) continue;
          ++wrong;
        }
        if (wrong * this->rate < this->preamblelen)
        {
          this->state = this->skip;
        }
        ++this->now;
        if (this->now ==  this->preamblelen) this->now = 0;
      }
      if (flag)
      //printf("findpreamble_cpp: %.10f\n",(double(clock()-start)/CLOCKS_PER_SEC)/noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace PHY */
} /* namespace gr */
