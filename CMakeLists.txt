cmake_minimum_required(VERSION 2.4)

project(prepar3d)

find_package(PythonLibs 3.5 REQUIRED)
find_package(Boost REQUIRED COMPONENTS filesystem system regex python)

include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${Boost_INCLUDE_DIRS})

# SimConnect stuff
find_path(SIMCONNECT_INCLUDE_DIR Inc/SimConnect.h)
include_directories(${SIMCONNECT_INCLUDE_DIR})

find_library(SIMCONNECT_LIBRARY NAMES SimConnect)

add_executable(script_loader tools/script_loader.cpp ) 
target_link_libraries(script_loader  ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})


file(GLOB SIMCONNECT_SOURCE_FILES src/simconnect/*.cpp)
file(GLOB UTIL_SOURCE_FILES src/util/*.cpp)

include_directories(src/simconnect src/util)

add_library(pyprepar3d SHARED ${SIMCONNECT_SOURCE_FILES} ${UTIL_SOURCE_FILES} ${Boost_LIBRARIES} ${PYTHON_LIBRARIES} ${SIMCONNECT_LIBRARY})
