#!/bin/bash
set -e
source /opt/ros/$1/setup.bash      # pass distro as arg, e.g. jazzy
source ~/ros2_ws/install/setup.bash
ros2 launch $2 $3                  # e.g. pkg file.launch.py
