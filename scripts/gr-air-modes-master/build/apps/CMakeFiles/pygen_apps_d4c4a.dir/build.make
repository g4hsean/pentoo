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

# Utility rule file for pygen_apps_d4c4a.

# Include the progress variables for this target.
include apps/CMakeFiles/pygen_apps_d4c4a.dir/progress.make

apps/CMakeFiles/pygen_apps_d4c4a: apps/modes_rx.exe
apps/CMakeFiles/pygen_apps_d4c4a: apps/modes_gui.exe
apps/CMakeFiles/pygen_apps_d4c4a: apps/uhd_modes.py.exe

apps/modes_rx.exe: ../apps/modes_rx
	$(CMAKE_COMMAND) -E cmake_progress_report /root/Desktop/scripts/gr-air-modes-master/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Shebangin modes_rx"
	cd /root/Desktop/scripts/gr-air-modes-master/build/apps && /usr/bin/python2 -c "import re; R=re.compile('^#!.*\$$\\n',flags=re.MULTILINE); open('/root/Desktop/scripts/gr-air-modes-master/build/apps/modes_rx.exe','w').write('#!/usr/bin/python2\\n'+R.sub('',open('/root/Desktop/scripts/gr-air-modes-master/apps/modes_rx','r').read()))"

apps/modes_gui.exe: ../apps/modes_gui
	$(CMAKE_COMMAND) -E cmake_progress_report /root/Desktop/scripts/gr-air-modes-master/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Shebangin modes_gui"
	cd /root/Desktop/scripts/gr-air-modes-master/build/apps && /usr/bin/python2 -c "import re; R=re.compile('^#!.*\$$\\n',flags=re.MULTILINE); open('/root/Desktop/scripts/gr-air-modes-master/build/apps/modes_gui.exe','w').write('#!/usr/bin/python2\\n'+R.sub('',open('/root/Desktop/scripts/gr-air-modes-master/apps/modes_gui','r').read()))"

apps/uhd_modes.py.exe: ../apps/uhd_modes.py
	$(CMAKE_COMMAND) -E cmake_progress_report /root/Desktop/scripts/gr-air-modes-master/build/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Shebangin uhd_modes.py"
	cd /root/Desktop/scripts/gr-air-modes-master/build/apps && /usr/bin/python2 -c "import re; R=re.compile('^#!.*\$$\\n',flags=re.MULTILINE); open('/root/Desktop/scripts/gr-air-modes-master/build/apps/uhd_modes.py.exe','w').write('#!/usr/bin/python2\\n'+R.sub('',open('/root/Desktop/scripts/gr-air-modes-master/apps/uhd_modes.py','r').read()))"

pygen_apps_d4c4a: apps/CMakeFiles/pygen_apps_d4c4a
pygen_apps_d4c4a: apps/modes_rx.exe
pygen_apps_d4c4a: apps/modes_gui.exe
pygen_apps_d4c4a: apps/uhd_modes.py.exe
pygen_apps_d4c4a: apps/CMakeFiles/pygen_apps_d4c4a.dir/build.make
.PHONY : pygen_apps_d4c4a

# Rule to build all files generated by this target.
apps/CMakeFiles/pygen_apps_d4c4a.dir/build: pygen_apps_d4c4a
.PHONY : apps/CMakeFiles/pygen_apps_d4c4a.dir/build

apps/CMakeFiles/pygen_apps_d4c4a.dir/clean:
	cd /root/Desktop/scripts/gr-air-modes-master/build/apps && $(CMAKE_COMMAND) -P CMakeFiles/pygen_apps_d4c4a.dir/cmake_clean.cmake
.PHONY : apps/CMakeFiles/pygen_apps_d4c4a.dir/clean

apps/CMakeFiles/pygen_apps_d4c4a.dir/depend:
	cd /root/Desktop/scripts/gr-air-modes-master/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /root/Desktop/scripts/gr-air-modes-master /root/Desktop/scripts/gr-air-modes-master/apps /root/Desktop/scripts/gr-air-modes-master/build /root/Desktop/scripts/gr-air-modes-master/build/apps /root/Desktop/scripts/gr-air-modes-master/build/apps/CMakeFiles/pygen_apps_d4c4a.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : apps/CMakeFiles/pygen_apps_d4c4a.dir/depend

