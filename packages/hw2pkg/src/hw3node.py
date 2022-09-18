#!/usr/bin/env python 3

import rospy
from std_msgs.msg import Float32
from mystery_package.msg import UnitsLabelled

class my_node:
    def __init__(self):
        self.total = 0
        self.pub_msg = UnitsLabelled()
        self.pub_msg.units = "meters"
        rospy.Subscriber('turtlesim/turtle1/pose', /turtlesim/pose, self.distance)
        self.pub_units = rospy.Publisher('new_topic',UnitsLabelled, queue_size = 10)
        
    def distance(self, msg):
        self.total += msg.data
        self.pub_msg.value = self.total
        self.pub_units.publish(self.pub_msg)

if __name__ == '__main__':
    rospy.init_node('my_node')
    my_node()
    rospy.spin
