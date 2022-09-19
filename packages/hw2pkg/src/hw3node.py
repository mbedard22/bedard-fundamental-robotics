#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from mystery_package.msg import UnitsLabelled
from turtlesim.msg import Pose

class my_node:
    def __init__(self):
        self.total = 0
        self.pub_msg = UnitsLabelled()
        self.pub_msg.units = "meters"
        rospy.Subscriber("/turtlesim/turtle1/pose", Pose, self.callback)
        self.pub_raw = rospy.Publisher("output", Float32, queue_size = 10)
        self.pub_units = rospy.Publisher("output", UnitsLabelled, queue_size = 10)
        
    def callback(self, msg):
        self.total += msg.x
        self.pub_msg.value = self.total
        self.pub_raw.publish(self.total)
        self.pub_units.publish(self.pub_msg)

if __name__ == '__main__':
    rospy.init_node('my_node')
    my_node()
    rospy.spin()
