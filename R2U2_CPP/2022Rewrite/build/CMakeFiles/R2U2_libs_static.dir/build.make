# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.11

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite/build

# Include any dependencies generated for this target.
include CMakeFiles/R2U2_libs_static.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/R2U2_libs_static.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/R2U2_libs_static.dir/flags.make

CMakeFiles/R2U2_libs_static.dir/CircularBuffer.cpp.o: CMakeFiles/R2U2_libs_static.dir/flags.make
CMakeFiles/R2U2_libs_static.dir/CircularBuffer.cpp.o: ../CircularBuffer.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/R2U2_libs_static.dir/CircularBuffer.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/R2U2_libs_static.dir/CircularBuffer.cpp.o -c /Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite/CircularBuffer.cpp

CMakeFiles/R2U2_libs_static.dir/CircularBuffer.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/R2U2_libs_static.dir/CircularBuffer.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite/CircularBuffer.cpp > CMakeFiles/R2U2_libs_static.dir/CircularBuffer.cpp.i

CMakeFiles/R2U2_libs_static.dir/CircularBuffer.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/R2U2_libs_static.dir/CircularBuffer.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite/CircularBuffer.cpp -o CMakeFiles/R2U2_libs_static.dir/CircularBuffer.cpp.s

CMakeFiles/R2U2_libs_static.dir/R2U2.cpp.o: CMakeFiles/R2U2_libs_static.dir/flags.make
CMakeFiles/R2U2_libs_static.dir/R2U2.cpp.o: ../R2U2.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/R2U2_libs_static.dir/R2U2.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/R2U2_libs_static.dir/R2U2.cpp.o -c /Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite/R2U2.cpp

CMakeFiles/R2U2_libs_static.dir/R2U2.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/R2U2_libs_static.dir/R2U2.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite/R2U2.cpp > CMakeFiles/R2U2_libs_static.dir/R2U2.cpp.i

CMakeFiles/R2U2_libs_static.dir/R2U2.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/R2U2_libs_static.dir/R2U2.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite/R2U2.cpp -o CMakeFiles/R2U2_libs_static.dir/R2U2.cpp.s

# Object files for target R2U2_libs_static
R2U2_libs_static_OBJECTS = \
"CMakeFiles/R2U2_libs_static.dir/CircularBuffer.cpp.o" \
"CMakeFiles/R2U2_libs_static.dir/R2U2.cpp.o"

# External object files for target R2U2_libs_static
R2U2_libs_static_EXTERNAL_OBJECTS =

libR2U2_libs_static.a: CMakeFiles/R2U2_libs_static.dir/CircularBuffer.cpp.o
libR2U2_libs_static.a: CMakeFiles/R2U2_libs_static.dir/R2U2.cpp.o
libR2U2_libs_static.a: CMakeFiles/R2U2_libs_static.dir/build.make
libR2U2_libs_static.a: CMakeFiles/R2U2_libs_static.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX static library libR2U2_libs_static.a"
	$(CMAKE_COMMAND) -P CMakeFiles/R2U2_libs_static.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/R2U2_libs_static.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/R2U2_libs_static.dir/build: libR2U2_libs_static.a

.PHONY : CMakeFiles/R2U2_libs_static.dir/build

CMakeFiles/R2U2_libs_static.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/R2U2_libs_static.dir/cmake_clean.cmake
.PHONY : CMakeFiles/R2U2_libs_static.dir/clean

CMakeFiles/R2U2_libs_static.dir/depend:
	cd /Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite /Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite /Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite/build /Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite/build /Users/gokul/Nok/r2u2ref/r2u2/R2U2_CPP/2022Rewrite/build/CMakeFiles/R2U2_libs_static.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/R2U2_libs_static.dir/depend

