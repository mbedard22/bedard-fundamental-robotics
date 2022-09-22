#!/usr/bin/env python3

import rospy
import math
from std_msgs.msg import Float32
from mystery_package.msg import UnitsLabelled
from turtlesim.msg import Pose

class my_node:
    def __init__(self):
        self.total = 0
        self.x = 0
        self.y = 0
        self.pub_msg = UnitsLabelled()
        self.pub_msg.units = "meters"
        rospy.Subscriber("/turtlesim/turtle1/pose", Pose, self.callback)
        self.pub_units = rospy.Publisher("output", UnitsLabelled, queue_size = 10)
        
    def callback(self, msg):
        self.total += math.sqrt(pow(msg.x - self.x, 2) + pow(msg.y - self.y,2))
        self.x = msg.x
        self.y = msg.y
        self.pub_msg.value = self.total
        self.pub_units.publish(self.pub_msg)

if __name__ == '__main__':
    rospy.init_node('my_node')
    my_node()
    rospy.spin()
