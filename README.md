# quack_overflow_ros
University of Memphis team ROS2 workspace template.

## Where to put files
Put ROS2 packages here:
```
~/ROS/ieee-senior-design-project/src/<your_package>
```
Must include `package.xml` + `CMakeLists.txt` (C++), or `setup.py` (Python). Do **not** commit `build/ install/ log/`.

## Launch (Emma)
Build workspace:
```bash
cd ~/ROS/ieee-senior-design-project
rosdep update && rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```

Run launch file:
```bash
ros2 launch <package> <file>.launch.py
```

Run nodes manually:
```bash
ros2 run <package> <node>
```
````markdown
