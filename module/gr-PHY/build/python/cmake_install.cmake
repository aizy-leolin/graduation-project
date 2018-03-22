# Install script for directory: /home/huangxf/graduation-project/module/gr-PHY/python

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/PHY" TYPE FILE FILES
    "/home/huangxf/graduation-project/module/gr-PHY/python/__init__.py"
    "/home/huangxf/graduation-project/module/gr-PHY/python/recv_bit.py"
    "/home/huangxf/graduation-project/module/gr-PHY/python/conv_encode.py"
    "/home/huangxf/graduation-project/module/gr-PHY/python/conv_decode.py"
    "/home/huangxf/graduation-project/module/gr-PHY/python/wave_to_bit.py"
    "/home/huangxf/graduation-project/module/gr-PHY/python/find_preamble.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/PHY" TYPE FILE FILES
    "/home/huangxf/graduation-project/module/gr-PHY/build/python/__init__.pyc"
    "/home/huangxf/graduation-project/module/gr-PHY/build/python/recv_bit.pyc"
    "/home/huangxf/graduation-project/module/gr-PHY/build/python/conv_encode.pyc"
    "/home/huangxf/graduation-project/module/gr-PHY/build/python/conv_decode.pyc"
    "/home/huangxf/graduation-project/module/gr-PHY/build/python/wave_to_bit.pyc"
    "/home/huangxf/graduation-project/module/gr-PHY/build/python/find_preamble.pyc"
    "/home/huangxf/graduation-project/module/gr-PHY/build/python/__init__.pyo"
    "/home/huangxf/graduation-project/module/gr-PHY/build/python/recv_bit.pyo"
    "/home/huangxf/graduation-project/module/gr-PHY/build/python/conv_encode.pyo"
    "/home/huangxf/graduation-project/module/gr-PHY/build/python/conv_decode.pyo"
    "/home/huangxf/graduation-project/module/gr-PHY/build/python/wave_to_bit.pyo"
    "/home/huangxf/graduation-project/module/gr-PHY/build/python/find_preamble.pyo"
    )
endif()

