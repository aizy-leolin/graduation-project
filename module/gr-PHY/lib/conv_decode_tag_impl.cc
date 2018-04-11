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
#include "conv_decode_tag_impl.h"
//#include <ctime>

namespace gr {
  namespace PHY {

    conv_decode_tag::sptr
    conv_decode_tag::make(const std::string &lengthtagname)
    {
      return gnuradio::get_initial_sptr
        (new conv_decode_tag_impl(lengthtagname));
    }

    /*
     * The private constructor
     */
    conv_decode_tag_impl::conv_decode_tag_impl(const std::string &lengthtagname)
      : gr::tagged_stream_block("conv_decode_tag",
              gr::io_signature::make(3, 3, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(unsigned char)), lengthtagname)
    {
      this->g0=0133;
      this->g1=0171;
      this->state= 1<<6;
      int tmp=0;
      for (int i =0; i<this->state<<1; ++i)
      {
        tmp = i & this->g0;
        this->encode0[i] = (tmp & 1) ^ ((tmp >> 1) & 1 ) ^ ((tmp >> 2) & 1 ) ^ ((tmp >> 3) & 1 ) ^ ((tmp >> 4) & 1 ) ^ ((tmp >> 5) & 1 ) ^ ((tmp >> 6) & 1 );
        tmp = i & this->g1;
        this->encode1[i] = (tmp & 1) ^ ((tmp >> 1) & 1 ) ^ ((tmp >> 2) & 1 ) ^ ((tmp >> 3) & 1 ) ^ ((tmp >> 4) & 1 ) ^ ((tmp >> 5) & 1 ) ^ ((tmp >> 6) & 1 );
      }
    }

    /*
     * Our virtual destructor.
     */
    conv_decode_tag_impl::~conv_decode_tag_impl()
    {
    }
    

    int
    conv_decode_tag_impl::calculate_output_stream_length(const gr_vector_int &ninput_items)
    {
      int noutput_items = (ninput_items[0]>>1) - 6;
      return noutput_items ;
    }

    int
    conv_decode_tag_impl::work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      if ((ninput_items[0]&1)>0)
        return 0;

      const float *in = (const float *) input_items[0];
      const float *minin = (const float *) input_items[1];
      const float *maxin = (const float *) input_items[2];
      unsigned char *out = (unsigned char *) output_items[0];
      //clock_t start = clock();

      float oldlikehood[1<<6] = {0};
      float likehood[1<<6] ={0};
      int **route=new int*[1<<6];
      for (int i=0;i<(1<<6);++i)
        route[i]=new int[ninput_items[0]>>1];
      int x,y,tx,ty;
      float likehood1,likehood2;
      float value[2][2];
      float now[2];
      for (int i=0; i<6; ++i)
      {
        value[0][0] = *(minin++);
        value[1][0] = *(minin++);
        value[0][1] = *(maxin++);
        value[1][1] = *(maxin++);
        now[0] = *(in++);
        now[1] = *(in++);

        for (int j=0;j<this->state;++j)
        {
          if ((j&((1<<(5-i))-1)) > 0)
          {
            likehood[j] = 100000000;
            route[j][i] = -1;
            continue;
          }

          x = (j&0x1F)<<1;
          tx = x | ((j&0x20)<<1);
          likehood[j] = oldlikehood[x] + abs(value[0][this->encode0[tx]]-now[0]) + abs(value[1][this->encode1[tx]]-now[1]);
          route[j][i] = x;
          if (i>0)
            if (route[x][i-1]<0)
              route[j][i]=-1;

        }

        memcpy((void *)oldlikehood,(void *)likehood,sizeof(float)*(1<<6));
      }

      for (int i = 6; i<(ninput_items[0]>>1) -6 ;++i )
      {

        value[0][0] = *(minin++);
        value[1][0] = *(minin++);
        value[0][1] = *(maxin++);
        value[1][1] = *(maxin++);
        now[0] = *(in++);
        now[1] = *(in++);

        for (int j=0;j<this->state;++j)
        {

          x = (j&0x1F)<<1;
          y = x | 0x1;
          tx = x | ((j&0x20)<<1);
          ty = tx | 0x1;

          likehood1 = oldlikehood[x] + abs(value[0][this->encode0[tx]]-now[0]) + abs(value[1][this->encode1[tx]]-now[1]);
          likehood2 = oldlikehood[y] + abs(value[0][this->encode0[ty]]-now[0]) + abs(value[1][this->encode1[ty]]-now[1]);

          if (route[x][i-1]<0)
          {
            if (route[y][i-1]<0)
            {
              likehood[j] = 100000000;
              route[j][i] =-1;
              continue;
            }
            likehood[j] = likehood2;
            route[j][i] = y;
            continue;
          }
          else if (route[y][i-1]<0)
          {
            likehood[j] = likehood1;
            route[j][i] = x;
            continue;
          }

          if (likehood1 < likehood2)
          {
            likehood[j] = likehood1;
            route[j][i] = x;
          }
          else
          {
            likehood[j] = likehood2;
            route[j][i] = y;
          }

        }

        memcpy((void *)oldlikehood,(void *)likehood,sizeof(float)*(1<<6));

      }

      int tmp = 0;
      tmp &= 0x0;
      tmp |= 1<<6;

      for (int i=(ninput_items[0]>>1)-6; i<(ninput_items[0]>>1); ++i )
      {
        value[0][0] = *(minin++);
        value[1][0] = *(minin++);
        value[0][1] = *(maxin++);
        value[1][1] = *(maxin++);
        now[0] = *(in++);
        now[1] = *(in++);
        tmp |= tmp>>1;

        for (int j=0;j<this->state;++j)
        { 

          if ((j&tmp)>0)
          {
            likehood[j] = 100000000;
            route[j][i] = -1;
            continue;
          }


          x = (j&0x1F)<<1;
          y = x | 0x1;
          tx = x;
          ty = y;

          likehood1 = oldlikehood[x] + abs(value[0][this->encode0[tx]]-now[0]) + abs(value[1][this->encode1[tx]]-now[1]);
          likehood2 = oldlikehood[y] + abs(value[0][this->encode0[ty]]-now[0]) + abs(value[1][this->encode1[ty]]-now[1]);

          if (route[x][i-1]<0)
          {
            if (route[y][i-1]<0)
            {
              likehood[j] = 100000000;
              route[j][i] =-1;
              continue;
            }
            likehood[j] = likehood2;
            route[j][i] = y;
            continue;
          }
          else if (route[y][i-1]<0)
          {
            likehood[j] = likehood1;
            route[j][i] = x;
            continue;
          }

          if (likehood1 < likehood2)
          {
            likehood[j] = likehood1;
            route[j][i] = x;
          }
          else
          {
            likehood[j] = likehood2;
            route[j][i] = y;
          }

        }

        memcpy((void *)oldlikehood,(void *)likehood,sizeof(float)*(1<<6));

      }

      int beststate = 0;
      for (int i=(ninput_items[0]>>1)-1; i>=((ninput_items[0]>>1)-6); --i)
      {
        beststate = route[beststate][i];
      }
      for (int i=(ninput_items[0]>>1)-7; i>=0; --i)
      {
        *(out+i) = (beststate>>5);
        beststate = route[beststate][i];
      }

      for (int i=0;i<(1<<6);++i)
        delete route[i];
      delete route;
      // Do <+signal processing+>

      // Tell runtime system how many output items we produced.
      //printf("conv_decode: %.10f\n",(double(clock()-start)/CLOCKS_PER_SEC)/ninput_items[0]);
      return (ninput_items[0]>>1)-6;
    }

  } /* namespace PHY */
} /* namespace gr */

