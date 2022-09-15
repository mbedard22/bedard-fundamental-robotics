#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class Talker:
    def __init__(self):
        self.pub = rospy.Publisher('turtlesim/turtle1/cmd_vel', geometry_msgs/Twist, queue_size=10)

    def forward(self):
        
        velocity_msg = Twist()
        velocity_msg = {linear: {x: 1, y: 0, z: 0}}
        self.pub.publish(velocity_msg)
    
    def turn(self:
    
        velocity_msg = Twist()
        velocity_msg = {linear: {x: 0, y: 0, z: 1}}
        self.pub.publish(velocity_msg)


if __name__=='__main__':
        try:
            rospy.init_node('talker',anonymous=True)
            t=Talker()
            rate=rospy.Rate(1)
            while not rospy.is_shutdown():
                for i in range 3
                t.forward()
                t.turn()
                rate.sleep()

        except rospy.ROSInterruptException:
            pass
