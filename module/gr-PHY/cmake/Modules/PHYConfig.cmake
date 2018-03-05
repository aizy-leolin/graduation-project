INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_PHY PHY)

FIND_PATH(
    PHY_INCLUDE_DIRS
    NAMES PHY/api.h
    HINTS $ENV{PHY_DIR}/include
        ${PC_PHY_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    PHY_LIBRARIES
    NAMES gnuradio-PHY
    HINTS $ENV{PHY_DIR}/lib
        ${PC_PHY_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(PHY DEFAULT_MSG PHY_LIBRARIES PHY_INCLUDE_DIRS)
MARK_AS_ADVANCED(PHY_LIBRARIES PHY_INCLUDE_DIRS)

