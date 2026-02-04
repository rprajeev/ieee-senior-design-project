import time

import rclpy
from rclpy.node import Node

from ..mecanum_vehicle import MecanumVehicle


class MecanumNode(Node):
    def __init__(self):
        super().__init__('mecanum_node')

        self.vehicle = MecanumVehicle()

        self.start_time = time.time()

        # Run autonomous loop at 10 Hz
        self.timer = self.create_timer(0.1, self.autonomous_loop)

        self.get_logger().info("Mecanum autonomous node started")

    def autonomous_loop(self):
        elapsed = time.time() - self.start_time

        if elapsed < 3.0:
            self.vehicle.forward(0.4)
        elif elapsed < 5.0:
            self.vehicle.rotate_cw(0.4)
        else:
            self.vehicle.stop()


def main():
    rclpy.init()
    node = MecanumNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
