from setuptools import setup

package_name = 'movement'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rohith',
    maintainer_email='rohith@example.com',
    description='Mecanum wheel movement node',
    license='Apache License 2.0',
    tests_require=['pytest','setuptools'],
    entry_points={
        'console_scripts': [
            'mecanum_node = movement.mecanum_node:main',
        ],
    },
)
