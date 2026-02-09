set -e

source /opt/ros/jazzy/setup.bash

# removes old built files
rm -rf build install log

colcon build

source install/setup.bash

