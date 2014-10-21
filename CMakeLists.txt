cmake_minimum_required(VERSION 2.4)

project(prepy3d_tools)

find_package(PythonLibs 2.7 REQUIRED)
find_package(Boost REQUIRED COMPONENTS filesystem system regex )

include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${Boost_INCLUDE_DIRS})

add_executable(script_loader tools/main.cpp ) 
target_link_libraries(script_loader  ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})