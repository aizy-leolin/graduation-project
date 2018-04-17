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
#include "wave_to_float_single_cpp_impl.h"

namespace gr {
  namespace PHY {

    wave_to_float_single_cpp::sptr
    wave_to_float_single_cpp::make(int decim)
    {
      return gnuradio::get_initial_sptr
        (new wave_to_float_single_cpp_impl(decim));
    }

    /*
     * The private constructor
     */
    wave_to_float_single_cpp_impl::wave_to_float_single_cpp_impl(int decim)
      : gr::sync_decimator("wave_to_float_single_cpp",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)), decim),decim(decim)
    {
      len = 0;
      maxlen = 10000;
      state = false;
      sortstate = false;
      cache = NULL;
      maxsplitdis = 0;
      maxsplitpos = 0;
      timecnt = 0;
      splitlen = 1000;
      file.open("log.txt");
    }

    /*
     * Our virtual destructor.
     */
    wave_to_float_single_cpp_impl::~wave_to_float_single_cpp_impl()
    {
    }

    float wave_to_float_single_cpp_impl::abs(float x)
    {
      if (x>0) return x;
      else return -x;
    }

    float wave_to_float_single_cpp_impl::maxsplit(const float *in)
    {
      float maxdis = 0,dis,mindis;
      int maxpos = 0,minpos;
      // for (int x = 0; x < 10;++x)
      //   file<<*(in+x)<<std::endl;
      for (int x=0; x<9; ++x)
      {
        dis = this->abs(*(in+x)-*(in+x+1));
        if (dis > maxdis)
        {
          maxdis = dis;
          maxpos = x + 1;
        }
      }

      if (this->state)
      {
        if ((maxdis > this->maxsplitdis)||(maxdis * 10 > (this->valuemax - this->valuemin)*0.3))
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
      // file<<"maxsplitpos: "<<this->maxsplitpos<<std::endl;
      //this->maxsplitpos = 9;
      float ans=0;
      if (this->cache==NULL)
      {
        this->cache = new float[decim];
        memcpy(this->cache,in,sizeof(float)*decim);
        for (int x=0;x<10;++x) ans+=*(in+x);
        // for (int x=6;x<9;++x) ans+=*(in+x);
        // mindis = this->abs(*(in)-*(in+1));
        // minpos = 1;
        // for (int x=1;x<9;++x)
        // {
        //   dis = this->abs(*(in+x+1)-*(in+x));
        //   if (dis<mindis)
        //   {
        //     mindis = dis;
        //     minpos = x+1;
        //   }
        // }
        // ans = *(in+minpos);
        // file<<"minpos: "<<minpos<<"  ans: "<<ans<<std::endl<<std::endl; 
        return ans;
      }
      else
      {
        for (int x=this->maxsplitpos; x<10; ++x) ans += *(this->cache+x);
        for (int x=0; x<this->maxsplitpos; ++x) ans += *(in+x);
        // if (this->maxsplitpos==9) {mindis = this->abs(*(in)-*(this->cache+9));minpos = 0;}
        // else {mindis = this->abs(*(this->cache+this->maxsplitpos+1)-*(this->cache+this->maxsplitpos)); minpos = this->maxsplitpos + 1;};
        // for (int x = this->maxsplitpos+1;x<10;++x)
        // {
        //   if (x==9)
        //     dis = this->abs(*(in)-*(this->cache+x));
        //   else
        //     dis = this->abs(*(this->cache+x)-*(this->cache+x+1));
        //   if (dis<mindis)
        //   {
        //     mindis = dis;
        //     if (x==9) minpos = 0;
        //     else minpos = x+1;
        //   }
        // }
        // for (int x=0;x<this->maxsplitpos-1;++x)
        // {
        //   dis = this->abs(*(in+x)-*(in+x+1));
        //   if (dis<mindis)
        //   {
        //     mindis = dis;
        //     minpos = x+1;
        //   }
        // }
        // if (minpos<this->maxsplitpos) ans = *(in + minpos);
        // else ans = *(this->cache+minpos);

        memcpy(this->cache,in,sizeof(float)*decim);
        // file<<"minpos: "<<minpos<<"ans: "<<ans<<"   mindis: "<<mindis<<std::endl<<std::endl;
      // file<<"ans: "<<ans<<std::endl<<std::endl;
        return ans;
      }
    }

    bool pairsort(const std::pair<float,int> a,const std::pair<float,int> b)
    {
      return a.first > b.first;
    }

    float wave_to_float_single_cpp_impl::maxsplit2(const float *in)
    {
      float maxdis = 0,dis,mindis;
      int maxpos = 0,minpos;
      // for (int x = 0; x < 10;++x)
      //   file<<*(in+x)<<std::endl;
      if (this->cache!=NULL) maxdis = this->abs(*in - *(this->cache+9));
      for (int x=0; x<9; ++x)
      {
        dis = this->abs(*(in+x)-*(in+x+1));
        if (dis > maxdis)
        {
          maxdis = dis;
          maxpos = x + 1;
        }
      }

      if (this->state)
      {
        if (!this->sortstate)
        {
          sort(record.begin(),record.end(),pairsort);
          int cnt[10]={0};
          for (int i=0;i< record.size()*0.2;++i)
          {
            ++cnt[record[i].second];
          }
          this->maxsplitpos = 0;
          for (int i = 1; i< 10; ++i)
            if (cnt[i]>cnt[this->maxsplitpos]) this->maxsplitpos = i;
          this->sortstate = true;

        }
        // if ((maxdis > this->maxsplitdis)||(maxdis * 10 > (this->valuemax - this->valuemin)*0.3))
        // {
        //   this->maxsplitdis = maxdis * 0.1 + this->maxsplitdis * 0.9;
        //   this->maxsplitpos = maxpos;
        // }
      }
      else
      {
        if (maxdis > this->maxsplitdis)
        {
          this->maxsplitdis = maxdis;
          this->maxsplitpos = maxpos;
        }
        record.push_back(std::make_pair<float,int>(maxdis,maxpos));
      }
      // file<<"maxsplitpos: "<<this->maxsplitpos<<std::endl;
      //this->maxsplitpos = 9;
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
        // file<<"minpos: "<<minpos<<"ans: "<<ans<<"   mindis: "<<mindis<<std::endl<<std::endl;
      // file<<"ans: "<<ans<<std::endl<<std::endl;
        return ans;
      }
    }


    float wave_to_float_single_cpp_impl::maxsplit3(const float *in)
    {
      float maxdis = 0,dis,mindis;
      int maxpos = 0,minpos;
      // for (int x = 0; x < 10;++x)
      //   file<<*(in+x)<<std::endl;
      if (this->cache!=NULL) maxdis = this->abs(*in - *(this->cache+9));
      for (int x=0; x<9; ++x)
      {
        dis = this->abs(*(in+x)-*(in+x+1));
        if (dis > maxdis)
        {
          maxdis = dis;
          maxpos = x + 1;
        }
      }

      // if (this->timecnt == 0)
      // {
      //   this->maxsplitdis = this->maxsplitdis / 2;
      // }
      this->maxsplitdis = this->maxsplitdis * 0.9998;
      if (maxdis > this->maxsplitdis)
      {
        this->maxsplitdis = maxdis;
        this->maxsplitpos = maxpos;
      }
      // ++this->timecnt;
      // if (this->timecnt == this->splitlen) this->timecnt = 0;
      
      // file<<"maxsplitpos: "<<this->maxsplitpos<<std::endl;
      // file<<"maxsplitdis: "<<this->maxsplitdis<<std::endl;
      // file<<"maxvalue: "<<this->valuemax<<std::endl;
      // file<<"minvalue: "<<this->valuemin<<std::endl;
      //this->maxsplitpos = 9;
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
        // file<<"minpos: "<<minpos<<"ans: "<<ans<<"   mindis: "<<mindis<<std::endl<<std::endl;
      // file<<"ans: "<<ans<<std::endl<<std::endl;
        return ans;
      }
    }

    int
    wave_to_float_single_cpp_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float*) input_items[0];
      float *out = (float *) output_items[0];
      // Do <+signal processing+>
      float tot;
      //clock_t start = clock();
      for (int i=0; i<noutput_items; ++i)
      {
        if (this->decim == 1)
          tot = *(in++);
        else
        {
          // tot = this->maxsplit(in);
          // tot = this->maxsplit2(in);
          tot = this->maxsplit3(in);
          in += this->decim;
        }

        if (this->len < this->maxlen)
        {
          if (this->len == 0)
          {
            *(out++) = 0;
            this->valuemin = tot;
            this->valuemax = tot;
            ++this->len;
            continue;
          }
          *(out++) = (tot-this->valuemin)/(this->valuemax-this->valuemin+0.000000000000001);
          ++this->len;
          if (tot > this->valuemax)
            this->valuemax = this->valuemax * 0.2 + tot * 0.8;
          if (tot < this->valuemin)
            this->valuemin = this->valuemin * 0.5 + tot * 0.5;
          continue;
        }
        this->state = true;
        // file<<"tot: "<<(tot-this->valuemin)/(this->valuemax-this->valuemin+0.000000000000001)<<std::endl<<std::endl;
        if (this->abs((tot-this->valuemin)/(this->valuemax-this->valuemin+0.000000000000001)-0.5)<0.05) this->maxsplitdis *= 0.9;
        *(out++) = (tot-this->valuemin)/(this->valuemax-this->valuemin+0.000000000000001);

        if (tot > (this->valuemax * 0.5 + this->valuemin * 0.5))
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

