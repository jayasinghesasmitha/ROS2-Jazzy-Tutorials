import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class ZeroTwist(Node):
    def __init__(self):
        super().__init__('zero_twist')
        self.sub = self.create_subscription(String, 'is_stopped', self.callback, 10)
        self.pub = self.create_publisher(Twist, 'twist', 10)

    def callback(self, msg):
        if msg.data == "true":
            twist = Twist()
            self.pub.publish(twist)

def main():
    rclpy.init()
    rclpy.spin(ZeroTwist())
    rclpy.shutdown()
