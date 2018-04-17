# Install script for directory: /home/huangxf/graduation-project/module/gr-PHY/include/PHY

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/PHY" TYPE FILE FILES
    "/home/huangxf/graduation-project/module/gr-PHY/include/PHY/api.h"
    "/home/huangxf/graduation-project/module/gr-PHY/include/PHY/conv_encode_tag.h"
    "/home/huangxf/graduation-project/module/gr-PHY/include/PHY/float_to_bit_tag.h"
    "/home/huangxf/graduation-project/module/gr-PHY/include/PHY/conv_decode_tag.h"
    "/home/huangxf/graduation-project/module/gr-PHY/include/PHY/float_to_bit_cpp.h"
    "/home/huangxf/graduation-project/module/gr-PHY/include/PHY/wave_to_float_cpp.h"
    "/home/huangxf/graduation-project/module/gr-PHY/include/PHY/find_preamble_cpp.h"
    "/home/huangxf/graduation-project/module/gr-PHY/include/PHY/wave_to_float_single_cpp.h"
    "/home/huangxf/graduation-project/module/gr-PHY/include/PHY/conv_decode_tag_single.h"
    "/home/huangxf/graduation-project/module/gr-PHY/include/PHY/float_to_bit_single_cpp.h"
    "/home/huangxf/graduation-project/module/gr-PHY/include/PHY/writefloat.h"
    )
endif()

