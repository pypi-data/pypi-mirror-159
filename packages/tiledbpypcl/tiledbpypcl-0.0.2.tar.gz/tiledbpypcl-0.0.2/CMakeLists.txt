cmake_minimum_required(VERSION 3.4...3.18)
project(tiledbpypcl)

add_subdirectory(pybind11)
pybind11_add_module(tiledbpypcl src/main.cpp)

find_package(PCL 1.12 REQUIRED COMPONENTS common io tracking keypoints)
include_directories(${PCL_INCLUDE_DIR})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})
target_link_libraries(tiledbpypcl PRIVATE ${PCL_LIBRARIES})

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(tiledbpypcl
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
