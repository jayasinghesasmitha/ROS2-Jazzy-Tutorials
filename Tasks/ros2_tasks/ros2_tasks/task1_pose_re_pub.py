import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose

class PoseRepub(Node):
    def __init__(self):
        super().__init__('pose_re_pub')
        self.sub = self.create_subscription(PoseWithCovarianceStamped, 'pose_with_covariance_stamped', self.callback, 10)
        self.pub = self.create_publisher(Pose, 'pose', 10)

    def callback(self, msg):
        pose_msg = msg.pose.pose
        self.pub.publish(pose_msg)

def main():
    rclpy.init()
    rclpy.spin(PoseRepub())
    rclpy.shutdown()
