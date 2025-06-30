import rclpy
from rclpy.node import Node

class ParamSetter(Node):
    def __init__(self):
        super().__init__('params_setter')
        param = 'example_param'
        value = 'hello_ros'
        self.declare_parameter(param, value)
        self.get_logger().info(f'Set parameter {param} = {value}')

def main():
    rclpy.init()
    node = ParamSetter()

    # Keep node alive so it stays in parameter list
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()
