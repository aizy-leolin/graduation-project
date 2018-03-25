/* -*- c++ -*- */

#define PHY_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "PHY_swig_doc.i"

%{
#include "PHY/conv_encode_tag.h"
#include "PHY/float_to_bit_tag.h"
#include "PHY/conv_decode_tag.h"
%}


%include "PHY/conv_encode_tag.h"
GR_SWIG_BLOCK_MAGIC2(PHY, conv_encode_tag);

%include "PHY/float_to_bit_tag.h"
GR_SWIG_BLOCK_MAGIC2(PHY, float_to_bit_tag);
%include "PHY/conv_decode_tag.h"
GR_SWIG_BLOCK_MAGIC2(PHY, conv_decode_tag);
