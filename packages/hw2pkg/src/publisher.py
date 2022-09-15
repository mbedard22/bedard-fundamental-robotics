#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class Square:
    def __init__(self):
        self.pub = rospy.Publisher('/turtlesim/turtle1/cmd_vel', Twist, queue_size=10)

    def forward(self):
        velocity_msg = Twist()
        velocity_msg = 
        self.pub.publish(velocity_msg)
    
    def turn(self):
        velocity_msg = Twist()
        velocity_msg = 
        self.pub.publish(velocity_msg)

if __name__=='__main__':
    try:
        rospy.init_node('square',anonymous=True)
        s=Square()
        rate=rospy.Rate(1)
        while not rospy.is_shutdown():
            for i in range (3):
                s.forward()
                s.turn()
                rate.sleep()
    except rospy.ROSInterruptException:
        pass
