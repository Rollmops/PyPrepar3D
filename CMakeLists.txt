cmake_minimum_required(VERSION 2.6)

project(prepar3d)

find_package(PythonLibs 3.5 REQUIRED)
find_package(Boost REQUIRED COMPONENTS filesystem system regex python)

include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${Boost_INCLUDE_DIRS})

# SimConnect stuff
find_path(SIMCONNECT_INCLUDE_DIR Inc/SimConnect.h)
include_directories(${SIMCONNECT_INCLUDE_DIR})

find_library(SIMCONNECT_LIBRARY NAMES SimConnect)

# script loader

add_executable(script_loader src/tools/script_loader.cpp ) 
target_link_libraries(script_loader  ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})

# python module

file(GLOB SIMCONNECT_SOURCE_FILES src/simconnect/*.cpp)
file(GLOB UTIL_SOURCE_FILES src/util/*.cpp)

include_directories(src/simconnect src/util)

PYTHON_ADD_MODULE(simconnect SHARED ${SIMCONNECT_SOURCE_FILES} ${UTIL_SOURCE_FILES})

target_link_libraries(simconnect ${Boost_LIBRARIES} ${PYTHON_LIBRARIES} ${SIMCONNECT_LIBRARY})
