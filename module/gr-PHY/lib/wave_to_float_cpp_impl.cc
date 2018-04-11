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
#include "wave_to_float_cpp_impl.h"
//#include <ctime>
namespace gr {
  namespace PHY {

    wave_to_float_cpp::sptr
    wave_to_float_cpp::make(int decim)
    {
      return gnuradio::get_initial_sptr
        (new wave_to_float_cpp_impl(decim));
    }

    /*
     * The private constructor
     */
    wave_to_float_cpp_impl::wave_to_float_cpp_impl(int decim)
      : gr::sync_decimator("wave_to_float_cpp",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(3, 3, sizeof(float)), decim),decim(decim)
    {
      len = 0;
      maxlen = 10000;
      state = false;
      cache = NULL;
      maxsplitdis = 0;
      maxsplitpos = 0;
    }

    /*
     * Our virtual destructor.
     */
    /*float abs(float x)
    {
      if (x>0) return x;
      else return -x;
    }*/
    wave_to_float_cpp_impl::~wave_to_float_cpp_impl()
    {
    }

    float wave_to_float_cpp_impl::maxsplit(const float *in)
    {
      float maxdis = 0,dis;
      int maxpos = 0;
      for (int x=0; x<9; ++x)
      {
        dis = abs(*(in+x)-*(in+x+1));
        if (dis > maxdis)
        {
          maxdis = dis;
          maxpos = x + 1;
        }
      }

      if (this->state)
      {
        if ((maxdis > this->maxsplitdis)||(maxdis * 10 > (this->valuemax - this->valuemin)*0.5))
        {
          this->maxsplitdis = maxdis * 0.1 + this->maxsplitdis * 0.9;
          this->maxsplitpos = maxpos;
        }
      }
      else
      {
        if (maxdis > this->maxsplitdis)
        {
          this->maxsplitdis = maxdis;
          this->maxsplitpos = maxpos;
        }
      }
      float ans=0;
      if (this->cache==NULL)
      {
        this->cache = new float[decim];
        memcpy(this->cache,in,sizeof(float)*decim);
        for (int x=0;x<10;++x) ans+=*(in+x);
        return ans;
      }
      else
      {
        for (int x=this->maxsplitpos; x<10; ++x) ans += *(this->cache+x);
        for (int x=0; x<this->maxsplitpos; ++x) ans += *(in+x);
        memcpy(this->cache,in,sizeof(float)*decim);
        return ans;
      }


    }

    int
    wave_to_float_cpp_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float*) input_items[0];
      float *out = (float *) output_items[0];
      float *minout = (float *) output_items[1];
      float *maxout = (float *) output_items[2];
      // Do <+signal processing+>
      float tot;
      //clock_t start = clock();
      for (int i=0; i<noutput_items; ++i)
      {
        if (this->decim == 1)
          tot = *(in++);
        else
        {
          tot = this->maxsplit(in);
          in += this->decim;
        }

        if (this->len < this->maxlen)
        {
          if (this->len == 0)
          {
            *(minout++) = tot;
            *(maxout++) = tot;
            *(out++) = tot;
            this->valuemin = tot;
            this->valuemax = tot;
            ++this->len;
            continue;
          }
          *(minout++) = this->valuemin;
          *(maxout++) = this->valuemax;
          *(out++) = tot;
          if (tot > this->valuemax)
            this->valuemax = this->valuemax * 0.2 + tot * 0.8;
          if (tot < this->valuemin)
            this->valuemin = this->valuemin * 0.5 + tot * 0.5;
          continue;
        }
        this->state = true;
        *(minout++) = this->valuemin;
        *(maxout++) = this->valuemax;
        *(out++) = tot;

        if (tot > (this->valuemax * 0.3 + this->valuemin * 0.7))
          this->valuemax = this->valuemax * 0.9 + tot * 0.1;
        else
          this->valuemin = this->valuemin * 0.9 + tot * 0.1;
      }

      //printf("wave_to_float_cpp: %.10f\n",(double(clock()-start)/CLOCKS_PER_SEC)/noutput_items);
      // Tell runtime system how many output items we produced.
      //printf("outputlen: %d\n", noutput_items );
      return noutput_items;
    }

  } /* namespace PHY */
} /* namespace gr */

