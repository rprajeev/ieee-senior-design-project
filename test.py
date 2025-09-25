import rospy
from std_msgs.msg import String

def controller():
    rospy.init_node('controller', anonymous=True)
    pub = rospy.Publisher('cmd_vel', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        command_str = "move_forward at 0.5 m/s"
        rospy.loginfo("Publishing command: %s", command_str)
        pub.publish(command_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        controller()
    except rospy.ROSInterruptException:
        pass