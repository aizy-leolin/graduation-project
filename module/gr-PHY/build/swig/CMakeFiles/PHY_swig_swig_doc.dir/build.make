# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

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
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/huangxf/graduation-project/module/gr-PHY

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/huangxf/graduation-project/module/gr-PHY/build

# Utility rule file for PHY_swig_swig_doc.

# Include the progress variables for this target.
include swig/CMakeFiles/PHY_swig_swig_doc.dir/progress.make

swig/CMakeFiles/PHY_swig_swig_doc: swig/PHY_swig_doc.i


swig/PHY_swig_doc.i: swig/PHY_swig_doc_swig_docs/xml/index.xml
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/huangxf/graduation-project/module/gr-PHY/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating python docstrings for PHY_swig_doc"
	cd /home/huangxf/graduation-project/module/gr-PHY/docs/doxygen && /usr/bin/python2 -B /home/huangxf/graduation-project/module/gr-PHY/docs/doxygen/swig_doc.py /home/huangxf/graduation-project/module/gr-PHY/build/swig/PHY_swig_doc_swig_docs/xml /home/huangxf/graduation-project/module/gr-PHY/build/swig/PHY_swig_doc.i

swig/PHY_swig_doc_swig_docs/xml/index.xml: swig/_PHY_swig_doc_tag
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/huangxf/graduation-project/module/gr-PHY/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating doxygen xml for PHY_swig_doc docs"
	cd /home/huangxf/graduation-project/module/gr-PHY/build/swig && ./_PHY_swig_doc_tag
	cd /home/huangxf/graduation-project/module/gr-PHY/build/swig && /usr/bin/doxygen /home/huangxf/graduation-project/module/gr-PHY/build/swig/PHY_swig_doc_swig_docs/Doxyfile

PHY_swig_swig_doc: swig/CMakeFiles/PHY_swig_swig_doc
PHY_swig_swig_doc: swig/PHY_swig_doc.i
PHY_swig_swig_doc: swig/PHY_swig_doc_swig_docs/xml/index.xml
PHY_swig_swig_doc: swig/CMakeFiles/PHY_swig_swig_doc.dir/build.make

.PHONY : PHY_swig_swig_doc

# Rule to build all files generated by this target.
swig/CMakeFiles/PHY_swig_swig_doc.dir/build: PHY_swig_swig_doc

.PHONY : swig/CMakeFiles/PHY_swig_swig_doc.dir/build

swig/CMakeFiles/PHY_swig_swig_doc.dir/clean:
	cd /home/huangxf/graduation-project/module/gr-PHY/build/swig && $(CMAKE_COMMAND) -P CMakeFiles/PHY_swig_swig_doc.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/PHY_swig_swig_doc.dir/clean

swig/CMakeFiles/PHY_swig_swig_doc.dir/depend:
	cd /home/huangxf/graduation-project/module/gr-PHY/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/huangxf/graduation-project/module/gr-PHY /home/huangxf/graduation-project/module/gr-PHY/swig /home/huangxf/graduation-project/module/gr-PHY/build /home/huangxf/graduation-project/module/gr-PHY/build/swig /home/huangxf/graduation-project/module/gr-PHY/build/swig/CMakeFiles/PHY_swig_swig_doc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/PHY_swig_swig_doc.dir/depend

