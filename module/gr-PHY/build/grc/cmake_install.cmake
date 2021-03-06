# Install script for directory: /home/huangxf/graduation-project/module/gr-PHY/grc

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_recv_bit.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_conv_encode.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_conv_decode.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_wave_to_bit.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_find_preamble.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_conv_encode_tag.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_wave_to_float.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_float_to_bit.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_float_to_bit_tag.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_conv_decode_tag.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_float_to_bit_cpp.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_wave_to_float_cpp.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_find_preamble_cpp.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_wave_to_float_single_cpp.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_conv_decode_tag_single.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_float_to_bit_single_cpp.xml"
    "/home/huangxf/graduation-project/module/gr-PHY/grc/PHY_writefloat.xml"
    )
endif()

