#!/usr/bin/env python3

import rospy
import math
from std_msgs.msg import Float32
from mystery_package.msg import UnitsLabelled
from turtlesim.msg import Pose

class conversion_node:
    def __init__(self):
        if rospy.has_param("unit_convert"):
            self.unit = rospy.get_param("unit_convert")
        else:
            self.unit = "default"

        rospy.Subscriber("output", UnitsLabelled, self.convert)
        self.pub_msg = UnitsLabelled()
        self.pub_msg.units = self.unit
        self.pub_units = rospy.Publisher("outputhw4", UnitsLabelled, queue_size = 10)
    
    def convert(self, msg):
        if(self.unit == "meters"):
            self.pub_msg = msg.value
            self.pub_units.publish(self.pub_msg)
        
        elif(self.unit == "feet"):
            self.pub_msg.value = msg.value * 3.28084
            self.pub_units.publish(self.pub_msg)
       
        elif(self.unit == "smoots"):
            self.pub_msg.value = msg.value * .587613
            self.pub_units.publish(self.pub_msg)
       
if __name__ == '__main__':
    rospy.init_node('conversion_node')
    conversion_node()
    rospy.spin()
