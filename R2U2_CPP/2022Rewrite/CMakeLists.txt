# cmake needs this line
cmake_minimum_required(VERSION 3.1)

# Define project name
project(R2U2)

include_directories(
    /usr/local/include/eigen3
    ${CMAKE_SOURCE_DIR}/
)

file(GLOB R2U2_libs
"${CMAKE_SOURCE_DIR}/*.cpp"
)
add_library(R2U2_libs_static STATIC ${R2U2_libs})

set_target_properties(R2U2_libs_static 
    PROPERTIES 
    CXX_STANDARD 14
    CXX_EXTENSIONS OFF
    CXX_STANDARD_REQUIRED ON
)


add_executable(R2U2.out R2U2.cpp)

set_target_properties(R2U2.out 
    PROPERTIES 
    CXX_STANDARD 14
    CXX_EXTENSIONS OFF
    CXX_STANDARD_REQUIRED ON
)

add_dependencies(R2U2.out R2U2_libs_static)
target_link_libraries(R2U2.out R2U2_libs_static)