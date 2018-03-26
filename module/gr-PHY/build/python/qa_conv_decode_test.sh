#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/huangxf/graduation-project/module/gr-PHY/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/huangxf/graduation-project/module/gr-PHY/build/python:$PATH
export LD_LIBRARY_PATH=/home/huangxf/graduation-project/module/gr-PHY/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/huangxf/graduation-project/module/gr-PHY/build/swig:$PYTHONPATH
/usr/bin/python2 /home/huangxf/graduation-project/module/gr-PHY/python/qa_conv_decode.py 
