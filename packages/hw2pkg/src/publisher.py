#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class Square:
    def __init__(self):
        self.pub = rospy.Publisher('/turtlesim/turtle1/cmd_vel', Twist, queue_size=10)

    def forward(self):
        velocity_msg = Twist()
        velocity_msg.linear.x = 4
        velocity_msg.linear.y = 0
        velocity_msg.linear.z = 0
        velocity_msg.angular.x = 0
        velocity_msg.angular.y = 0
        velocity_msg.angular.z = 0
        #rospy.loginfo(velocity_msg)
        self.pub.publish(velocity_msg)
    
    def turn(self):
        velocity_msg = Twist()
        velocity_msg.linear.x = 0
        velocity_msg.linear.y = 0
        velocity_msg.linear.z = 0
        velocity_msg.angular.x = 0
        velocity_msg.angular.y = 0
        velocity_msg.angular.z = 1.56
        #rospy.loginfo(velocity_msg)
        self.pub.publish(velocity_msg)

if __name__=='__main__':
    try:
        rospy.init_node('square',anonymous=True)
        s=Square()
        rate=rospy.Rate(1)
        while not rospy.is_shutdown():
            rate.sleep()
            s.forward()
            rate.sleep()
            rate.sleep()
            s.turn()
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
