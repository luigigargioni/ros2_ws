#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class PoseSubriberNode(Node):
    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subscriber_ = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10
        )
        self.get_logger().info("Pose subscriber has been started")

    def pose_callback(self, msg: Pose):
        self.get_logger().info("(X: " + str(msg.x) + ", Y: " + str(msg.y) + ")")


def main(args=None):
    rclpy.init(args=args)
    node = PoseSubriberNode()
    rclpy.spin(node)
    rclpy.shutdown()
