INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_ROUND round)

FIND_PATH(
    ROUND_INCLUDE_DIRS
    NAMES round/api.h
    HINTS $ENV{ROUND_DIR}/include
        ${PC_ROUND_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    ROUND_LIBRARIES
    NAMES gnuradio-round
    HINTS $ENV{ROUND_DIR}/lib
        ${PC_ROUND_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(ROUND DEFAULT_MSG ROUND_LIBRARIES ROUND_INCLUDE_DIRS)
MARK_AS_ADVANCED(ROUND_LIBRARIES ROUND_INCLUDE_DIRS)

