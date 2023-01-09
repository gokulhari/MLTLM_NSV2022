cmake_minimum_required(VERSION 3.16)
project(MLTLM LANGUAGES CXX)

set(ANTLR_SOURCE_DIR "/Users/gokul/Nok/antlr4-4.9.2/")

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug CACHE STRING "Build type" FORCE)
endif()

message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")

include_directories(
  ${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src
  ${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/atn
  ${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/dfa
  ${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/misc
  ${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/support
  ${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/tree
  ${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/tree/pattern
  ${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/tree/xpath
  ${CMAKE_SOURCE_DIR}/
)

file(GLOB libantlrcpp_SRC
  "${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/*.cpp"
  "${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/atn/*.cpp"
  "${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/dfa/*.cpp"
  "${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/misc/*.cpp"
  "${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/support/*.cpp"
  "${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/tree/*.cpp"
  "${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/tree/pattern/*.cpp"
  "${ANTLR_SOURCE_DIR}/runtime/Cpp/runtime/src/tree/xpath/*.cpp"
)

file(GLOB libMLTLM_SRC
"${CMAKE_SOURCE_DIR}/*.cpp"
)

add_library(antlr4_static STATIC ${libantlrcpp_SRC})
add_library(MLTLM_static STATIC ${libMLTLM_SRC})

set_target_properties(antlr4_static 
    PROPERTIES 
    CXX_STANDARD 14
    CXX_EXTENSIONS OFF
    CXX_STANDARD_REQUIRED ON
)

set_target_properties(MLTLM_static 
    PROPERTIES 
    CXX_STANDARD 14
    CXX_EXTENSIONS OFF
    CXX_STANDARD_REQUIRED ON
)

add_executable(main main2.cpp)

set_target_properties(main 
    PROPERTIES 
    CXX_STANDARD 14
    CXX_EXTENSIONS OFF
    CXX_STANDARD_REQUIRED ON
)

add_dependencies(main antlr4_static MLTLM_static)
target_link_libraries(main antlr4_static MLTLM_static)
