from setuptools import setup

package_name = 'mecanum_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rprajeev',
    maintainer_email='rprajeev@example.com',
    description='ROS2 mecanum robot control',
    license='MIT',
    entry_points={
        'console_scripts': [
            'mecanum_node = mecanum_robot.mecanum_node:main',
        ],
    },
)
