#!/usr/bin/env python3

from math import radians, sin, cos
import numpy
import rospy
from geometry_msgs.msg import Pose2D
from odometry_hw.msg import DistWheel

class odometry:
    def __init__(self):
        self.theta = 0
        self.x = 0
        self.y = 0
        self.pub_msg = Pose2D()
        rospy.Subscriber("dist_wheel", DistWheel, self.callback)
        self.pub_pose = rospy.Publisher("pose", Pose2D, queue_size = 10)
    
    def callback(self, msg):

        self.deltas = (msg.dist_wheel_left + msg.dist_wheel_right) / 2
        self.deltat = (msg.dist_wheel_right - msg.dist_wheel_left) / 0.1
        self.deltax = self.deltas * cos(self.theta + (self.deltat / 2))
        self.deltay = self.deltas * sin(self.theta + (self.deltat / 2))
        
        self.x += self.deltax
        self.y += self.deltay
        self.theta += self.deltat
        
        self.pub_msg.x = self.x
        self.pub_msg.y = self.y
        self.pub_msg.theta = self.theta
        self.pub_pose.publish(self.pub_msg)

if __name__ == '__main__':
    rospy.init_node('odometry')
    odometry()
    rospy.spin()
