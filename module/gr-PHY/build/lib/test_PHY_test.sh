#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/huangxf/graduation-project/module/gr-PHY/lib
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/huangxf/graduation-project/module/gr-PHY/build/lib:$PATH
export LD_LIBRARY_PATH=/home/huangxf/graduation-project/module/gr-PHY/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-PHY 
