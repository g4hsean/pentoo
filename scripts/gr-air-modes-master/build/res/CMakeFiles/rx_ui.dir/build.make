# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.2

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
CMAKE_SOURCE_DIR = /root/Desktop/scripts/gr-air-modes-master

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /root/Desktop/scripts/gr-air-modes-master/build

# Utility rule file for rx_ui.

# Include the progress variables for this target.
include res/CMakeFiles/rx_ui.dir/progress.make

res/CMakeFiles/rx_ui: res/modes_rx_ui.py

res/modes_rx_ui.py: res/modes_rx_ui_borked.py
	$(CMAKE_COMMAND) -E cmake_progress_report /root/Desktop/scripts/gr-air-modes-master/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating modes_rx_ui.py"
	cd /root/Desktop/scripts/gr-air-modes-master/build/res && sed s/from\ qwt.*\ import/from\ PyQt4.Qwt5.Qwt\ import/ /root/Desktop/scripts/gr-air-modes-master/build/res/modes_rx_ui_borked.py > /root/Desktop/scripts/gr-air-modes-master/build/res/modes_rx_ui.py

res/modes_rx_ui_borked.py: ../res/modes_rx.ui
	$(CMAKE_COMMAND) -E cmake_progress_report /root/Desktop/scripts/gr-air-modes-master/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating modes_rx_ui_borked.py"
	cd /root/Desktop/scripts/gr-air-modes-master/build/res && /usr/bin/pyuic4 /root/Desktop/scripts/gr-air-modes-master/res/modes_rx.ui > /root/Desktop/scripts/gr-air-modes-master/build/res/modes_rx_ui_borked.py

rx_ui: res/CMakeFiles/rx_ui
rx_ui: res/modes_rx_ui.py
rx_ui: res/modes_rx_ui_borked.py
rx_ui: res/CMakeFiles/rx_ui.dir/build.make
.PHONY : rx_ui

# Rule to build all files generated by this target.
res/CMakeFiles/rx_ui.dir/build: rx_ui
.PHONY : res/CMakeFiles/rx_ui.dir/build

res/CMakeFiles/rx_ui.dir/clean:
	cd /root/Desktop/scripts/gr-air-modes-master/build/res && $(CMAKE_COMMAND) -P CMakeFiles/rx_ui.dir/cmake_clean.cmake
.PHONY : res/CMakeFiles/rx_ui.dir/clean

res/CMakeFiles/rx_ui.dir/depend:
	cd /root/Desktop/scripts/gr-air-modes-master/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /root/Desktop/scripts/gr-air-modes-master /root/Desktop/scripts/gr-air-modes-master/res /root/Desktop/scripts/gr-air-modes-master/build /root/Desktop/scripts/gr-air-modes-master/build/res /root/Desktop/scripts/gr-air-modes-master/build/res/CMakeFiles/rx_ui.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : res/CMakeFiles/rx_ui.dir/depend

