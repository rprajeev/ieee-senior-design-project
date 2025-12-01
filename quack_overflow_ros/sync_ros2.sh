#!/bin/bash
set -e
cd ~/ros2_ws/src
git pull
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release
