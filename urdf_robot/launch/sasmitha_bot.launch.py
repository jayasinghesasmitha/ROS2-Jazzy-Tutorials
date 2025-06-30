from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so', 'worlds/four_walls.world'],
            output='screen'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            arguments=['urdf/sasmitha_bot.xacro'],
            output='screen'),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'sasmitha_bot', '-file', 'urdf/sasmitha_bot.xacro'],
            output='screen'),

        Node(
            package='urdf',
            executable='sasmitha_bot_node',
            name='sasmitha_bot_node',
            output='screen'),
    ])