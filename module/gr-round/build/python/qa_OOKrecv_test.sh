#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/huangxf/test/gr-round/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/huangxf/test/gr-round/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/huangxf/test/gr-round/build/swig:$PYTHONPATH
/usr/bin/python2 /home/huangxf/test/gr-round/python/qa_OOKrecv.py 
