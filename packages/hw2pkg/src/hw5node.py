#!/usr/bin/env python3

from math import radians, sin, cos
import numpy
import rospy
from duckietown_msgs.msg import Vector2D

class transformer:
    def __init__(self):
        self.pub_msg = Vector2D()
        self.pub_robot = rospy.Publisher("/robot_coord", Vector2D, queue_size = 10)
        self.pub_world = rospy.Publisher("/world_coord", Vector2D, queue_size = 10)
        rospy.Subscriber("/sensor_coord", Vector2D, self.callback)
        self.RTS = numpy.matrix([[-1, 0, -1], [0, -1, 0], [0, 0, 1]])
        self.WTR = numpy.matrix([[-1/numpy.sqrt(2), -1/numpy.sqrt(2), 5], [1/numpy.sqrt(2), -1/numpy.sqrt(2), 3], [0, 0, 1]])

    def callback(self, msg):
        v = numpy.matrix([[msg.x], [msg.y], [1]])
        new_v = self.RTS * v
        self.pub_msg.x = new_v[0, 0]
        self.pub_msg.y = new_v[1, 0]
        self.pub_robot.publish(self.pub_msg)
        new_v2 = self.WTR * new_v
        self.pub_msg.x = new_v2[0,0]
        self.pub_msg.y = new_v2[1,0]
        self.pub_world.publish(self.pub_msg)

if __name__ == '__main__':
    rospy.init_node('transformer')
    transformer()
    rospy.spin()
