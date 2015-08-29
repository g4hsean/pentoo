# Install script for directory: /root/Desktop/scripts/gr-air-modes-master/python

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
  set(CMAKE_INSTALL_SO_NO_EXE "0")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib64/python2.7/site-packages/air_modes" TYPE FILE FILES
    "/root/Desktop/scripts/gr-air-modes-master/python/__init__.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/altitude.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/az_map.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/cpr.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/html_template.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/mlat.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/exceptions.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/flightgear.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/gui_model.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/kml.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/parse.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/msprint.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/radio.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/raw_server.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/rx_path.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/sbs1.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/sql.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/types.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/zmq_socket.py"
    "/root/Desktop/scripts/gr-air-modes-master/python/Quaternion.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib64/python2.7/site-packages/air_modes" TYPE FILE FILES
    "/root/Desktop/scripts/gr-air-modes-master/build/python/__init__.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/altitude.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/az_map.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/cpr.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/html_template.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/mlat.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/exceptions.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/flightgear.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/gui_model.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/kml.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/parse.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/msprint.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/radio.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/raw_server.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/rx_path.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/sbs1.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/sql.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/types.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/zmq_socket.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/Quaternion.pyc"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/__init__.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/altitude.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/az_map.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/cpr.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/html_template.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/mlat.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/exceptions.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/flightgear.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/gui_model.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/kml.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/parse.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/msprint.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/radio.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/raw_server.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/rx_path.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/sbs1.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/sql.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/types.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/zmq_socket.pyo"
    "/root/Desktop/scripts/gr-air-modes-master/build/python/Quaternion.pyo"
    )
endif()

