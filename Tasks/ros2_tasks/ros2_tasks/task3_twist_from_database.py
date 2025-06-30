import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import csv
import importlib.resources
import ros2_tasks.data  # This is your CSV resource package

class TwistPublisher(Node):
    def __init__(self):
        super().__init__('twist_from_database')
        self.publisher = self.create_publisher(Twist, 'twist_from_database', 20)
        self.timer = self.create_timer(0.1, self.publish_twist)
        
        # Open the values.csv file using importlib.resources
        with importlib.resources.files(ros2_tasks.data).joinpath('values.csv').open('r') as f:
            self.lines = list(csv.reader(f))
        self.index = 0

    def publish_twist(self):
        if self.index >= len(self.lines):
            self.get_logger().info("Finished reading CSV.")
            self.destroy_timer(self.timer)
            return

        line = self.lines[self.index]
        self.index += 1

        twist = Twist()
        values = list(map(float, line))
        twist.linear.x, twist.linear.y, twist.linear.z = values[:3]
        twist.angular.x, twist.angular.y, twist.angular.z = values[3:]
        self.publisher.publish(twist)

def main():
    rclpy.init()
    node = TwistPublisher()
    rclpy.spin(node)
    rclpy.shutdown()
