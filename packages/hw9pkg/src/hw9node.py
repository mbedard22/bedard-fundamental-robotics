#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32


class PID_controller:
    def __init__(self):
        self.kp = 0.15
        self.ki = 0.02
        self.kd = 0.5
        self.output = 0
        self.laste = 30
        self.cumError = 0
        self.rateError = 0
        self.pub = rospy.Publisher("/control_input", Float32, queue_size = 10)
        rospy.Subscriber("/error", Float32, self.callback)
        rospy.set_param("/controller_ready", "true")

    def callback(self, msg):
        self.cumError += msg.data * 0.1
        self.rateError = (msg.data - self.laste) / 0.1
        self.output = (self.kp * msg.data) + (self.ki * self.cumError) + (self.kd * self.rateError)
        self.laste = msg.data
        self.pub.publish(self.output)

if __name__ == "__main__":
    rospy.init_node("PID_controller", anonymous = True)
    PID_controller = PID_controller()
    rospy.spin()
