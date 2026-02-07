import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from movement.mecanum_vehicle import MecanumVehicle


class MecanumNode(Node):
    def __init__(self):
        super().__init__('mecanum_node')
        self.vehicle = MecanumVehicle()
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.cmd_vel_callback,
            10
        )
        self.get_logger().info('Mecanum node started and ready to receive /cmd_vel')

    def cmd_vel_callback(self, msg: Twist):
        vx = msg.linear.x     # forward/back
        vy = msg.linear.y     # strafe
        wz = msg.angular.z   # rotation

        # Simple mecanum mixing (not normalized yet)
        fl = vx - vy - wz
        fr = vx + vy + wz
        rl = vx + vy - wz
        rr = vx - vy + wz

        # Normalize wheel speeds
        max_val = max(abs(fl), abs(fr), abs(rl), abs(rr), 1.0)
        fl /= max_val
        fr /= max_val
        rl /= max_val
        rr /= max_val

        speed = max(abs(vx), abs(vy), abs(wz), 0.2)

        self.vehicle.drive(fl, fr, rl, rr, speed)


def main(args=None):
    rclpy.init(args=args)
    node = MecanumNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
