import rclpy
from rclpy.node import Node

class ParamReader(Node):
    def __init__(self):
        super().__init__('param_reader')
        self.declare_parameter('robot_name', 'default_bot')
        name = self.get_parameter('robot_name').get_parameter_value().string_value
        self.get_logger().info(f'Robot name: {name}')

def main():
    rclpy.init()
    ParamReader()
    rclpy.shutdown()
