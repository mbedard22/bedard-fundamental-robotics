#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class edge_finder:
    def __init__(self):
        self.original_image = np.zeros((240,640,3),dtype=np.uint8)
        self.white_image = np.zeros((240,640, 3), dtype=np.uint8)
        rospy.Subscriber("/image_cropped", Image, self.callback)
        rospy.Subscriber("/image_white", Image, self.callback_white)
        rospy.Subscriber("/image_yellow", Image, self.callback_yellow)
        
        self.pub_canny = rospy.Publisher("/image_edges", Image, queue_size = 10)
        self.pub_white = rospy.Publisher("/image_lines_white", Image, queue_size = 10)
        self.pub_yellow = rospy.Publisher("/image_lines_yellow", Image, queue_size = 10)
        self.pub_all = rospy.Publisher("/image_lines_all", Image, queue_size = 10)
        self.bridge = CvBridge()

    def callback(self, msg):
        self.original_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
    
    def callback_white(self, msg):
        self.white_image = self.bridge.imgmsg_to_cv2(msg, "mono8")

    def callback_yellow(self, msg):
        edges = cv2.Canny(self.original_image, 0, 500)
        output_edges = self.bridge.cv2_to_imgmsg(edges, "mono8")
        self.pub_canny.publish(output_edges)

        yellow_image = self.bridge.imgmsg_to_cv2(msg, "mono8")
        yellow_edges = cv2.bitwise_and(edges, yellow_image)
        yellow_lines = cv2.HoughLinesP(yellow_edges, rho = 1, theta = (np.pi/180), threshold = 40, minLineLength = 1, maxLineGap = 8)
        output_yellow = self.output_lines(self.original_image, yellow_lines)
        output_yellow = self.bridge.cv2_to_imgmsg(output_yellow, "bgr8")
        self.pub_yellow.publish(output_yellow)

        white_edges = cv2.bitwise_and(edges, self.white_image)
        white_lines = cv2.HoughLinesP(white_edges, rho = 1, theta = (np.pi/180), threshold = 40, minLineLength = 1, maxLineGap = 8)
        output_white = self.output_lines(self.original_image, white_lines)
        output_white = self.bridge.cv2_to_imgmsg(output_white, "bgr8")
        self.pub_white.publish(output_white)

    def output_lines(self, original_image, lines):
        output = np.copy(original_image)
        if lines is not None:
            for i in range(len(lines)):
                l = lines[i][0]
                cv2.line(output, (l[0],l[1]), (l[2],l[3]), (255,0,0), 2, cv2.LINE_AA)
                cv2.circle(output, (l[0],l[1]), 2, (0,255,0))
                cv2.circle(output, (l[2],l[3]), 2, (0,0,255))
        return output

if __name__ == "__main__":
    rospy.init_node("edge_finder", anonymous = True)
    edge_finder = edge_finder()
    rospy.spin()
