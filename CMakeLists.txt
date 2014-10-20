cmake_minimum_required(VERSION 2.4)

project(embedding_python)

set(PY_MODULE_FILES
src/module_simconnect.cpp)

message(STATUS "Files: ${SRC_FILES}")

find_package(PythonLibs 2.7 REQUIRED)
find_package(Boost REQUIRED COMPONENTS python filesystem system regex )

include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${Boost_INCLUDE_DIRS})

add_executable(script_loader src/main.cpp ) 
target_link_libraries(script_loader  ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})

add_library(ext_module SHARED ${PY_MODULE_FILES})
set_target_properties(ext_module PROPERTIES PREFIX "")
target_link_libraries(ext_module ${Boost_LIBRARIES} ${PYTHON_LIBRARIES} )