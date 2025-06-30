from setuptools import find_packages, setup

package_name = 'ros2_tasks'

setup(
    name=package_name,
    version='0.0.0',
    # packages=find_packages(exclude=['test']),
    packages=['ros2_tasks'],
    package_data={'ros2_tasks': ['data/*.csv']},

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages', ['resource/ros2_tasks']),
        ('share/ros2_tasks', ['package.xml']),
        ('share/ros2_tasks/launch', ['launch/test_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sasmitha-jayasinghe',
    maintainer_email='sasmitha.22@cse.mrt.ac.lk',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'pose_re_pub = ros2_tasks.task1_pose_re_pub:main',
        'params_setter = ros2_tasks.task2_params_setter:main',
        'twist_from_database = ros2_tasks.task3_twist_from_database:main',
        'zero_twist = ros2_tasks.task4_zero_twist:main',
        'param_reader = ros2_tasks.task6_param_reader:main',
        ],
    },

)
