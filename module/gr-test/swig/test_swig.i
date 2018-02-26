/* -*- c++ -*- */

#define TEST_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "test_swig_doc.i"

%{
#include "test/print_fb.h"
%}


%include "test/print_fb.h"
GR_SWIG_BLOCK_MAGIC2(test, print_fb);
