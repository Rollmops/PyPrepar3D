cmake_minimum_required(VERSION 2.4)

project(embedding_python)

file(GLOB SRC_FILES "src/*.cpp")

message(STATUS "Files: ${SRC_FILES}")

find_package(PythonLibs 2.7 REQUIRED)
find_package(Boost REQUIRED COMPONENTS filesystem system regex)

include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${Boost_INCLUDE_DIRS})

add_executable(py_embedding ${SRC_FILES}) 

target_link_libraries(py_embedding ${PYTHON_LIBRARIES} ${Boost_LIBRARIES})