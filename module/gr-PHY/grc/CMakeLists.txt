# Copyright 2011 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
install(FILES
    PHY_recv_bit.xml
    PHY_conv_encode.xml
    PHY_conv_decode.xml
    PHY_wave_to_bit.xml
    PHY_find_preamble.xml
    PHY_conv_encode_tag.xml
    PHY_wave_to_float.xml
    PHY_float_to_bit.xml
    PHY_float_to_bit_tag.xml
    PHY_conv_decode_tag.xml
    PHY_float_to_bit_cpp.xml
    PHY_wave_to_float_cpp.xml
    PHY_find_preamble_cpp.xml
    PHY_wave_to_float_single_cpp.xml
    PHY_conv_decode_tag_single.xml
    PHY_float_to_bit_single_cpp.xml
    PHY_writefloat.xml
    DESTINATION share/gnuradio/grc/blocks
)
