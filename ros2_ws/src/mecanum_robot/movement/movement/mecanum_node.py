import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class MecanumNode(Node):
    def __init__(self):
        super().__init__('mecanum_node')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info('Mecanum node started')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.5     # forward
        msg.linear.y = 0.0     # sideways
        msg.angular.z = 0.0   # rotation
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = MecanumNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
# ================================