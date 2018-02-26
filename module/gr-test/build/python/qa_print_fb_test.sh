#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/huangxf/test/gr-test/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/huangxf/test/gr-test/build/python:$PATH
export LD_LIBRARY_PATH=/home/huangxf/test/gr-test/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/huangxf/test/gr-test/build/swig:$PYTHONPATH
/usr/bin/python2 /home/huangxf/test/gr-test/python/qa_print_fb.py 
