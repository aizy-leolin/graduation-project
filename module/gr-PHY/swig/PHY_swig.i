/* -*- c++ -*- */

#define PHY_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "PHY_swig_doc.i"

%{
#include "PHY/conv_encode_tag.h"
#include "PHY/float_to_bit_tag.h"
#include "PHY/conv_decode_tag.h"
#include "PHY/float_to_bit_cpp.h"
#include "PHY/wave_to_float_cpp.h"
#include "PHY/find_preamble_cpp.h"
#include "PHY/wave_to_float_single_cpp.h"
#include "PHY/conv_decode_tag_single.h"
#include "PHY/float_to_bit_single_cpp.h"
%}


%include "PHY/conv_encode_tag.h"
GR_SWIG_BLOCK_MAGIC2(PHY, conv_encode_tag);

%include "PHY/float_to_bit_tag.h"
GR_SWIG_BLOCK_MAGIC2(PHY, float_to_bit_tag);
%include "PHY/conv_decode_tag.h"
GR_SWIG_BLOCK_MAGIC2(PHY, conv_decode_tag);
%include "PHY/float_to_bit_cpp.h"
GR_SWIG_BLOCK_MAGIC2(PHY, float_to_bit_cpp);

%include "PHY/wave_to_float_cpp.h"
GR_SWIG_BLOCK_MAGIC2(PHY, wave_to_float_cpp);
%include "PHY/find_preamble_cpp.h"
GR_SWIG_BLOCK_MAGIC2(PHY, find_preamble_cpp);

%include "PHY/wave_to_float_single_cpp.h"
GR_SWIG_BLOCK_MAGIC2(PHY, wave_to_float_single_cpp);

%include "PHY/conv_decode_tag_single.h"
GR_SWIG_BLOCK_MAGIC2(PHY, conv_decode_tag_single);
%include "PHY/float_to_bit_single_cpp.h"
GR_SWIG_BLOCK_MAGIC2(PHY, float_to_bit_single_cpp);
