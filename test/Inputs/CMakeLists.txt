# cmake needs this line
cmake_minimum_required(VERSION 3.1)

# Define project name
project(GenInputs)

include_directories(
    /usr/local/include/eigen3
)

add_executable(genInputsMLTLM.out genInputsMLTLM.cpp)

set_target_properties(genInputsMLTLM.out 
    PROPERTIES 
    CXX_STANDARD 14
    CXX_EXTENSIONS OFF
    CXX_STANDARD_REQUIRED ON
)
