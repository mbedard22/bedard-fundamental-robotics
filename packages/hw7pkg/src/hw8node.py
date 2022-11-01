#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class edge_finder:
    def __init__(self):
        rospy.Subscriber("/image_cropped", Image, self.callback)
        rospy.Subscriber("/image_white", Image, self.callback_white)
        rospy.Subscriber("/image_yellow", Image, self.callback_yellow)
        
        self.pub_canny = rospy.Publisher("/image_edges", Image, queue_size = 10)
        self.pub_white = rospy.Publisher("/image_lines_white", Image, queue_size = 10)
        self.pub_yellow = rospy.Publisher("/image_lines_yellow", Image, queue_size = 10)
        self.pub_all = rospy.Publisher("/image_lines_all", Image, queue_size = 10)
        self.bridge = CvBridge()

    def callback(self, msg):
        original_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
    
    def callback_white(self, msg):
        white_image = self.bridge.imgmsg_to_cv2(msg, "mono8")

    def callback_yellow(self, msg):
        edges = cv2.Cannyoriginal_image, 0, 100)
        output_edges = self.bridge.cv2_to_imgmsg(edges, "mono8")
        self.pub_canny.publish(output_edges)

        yellow_image = self.bridge.imgmsg_to_cv2(msg, "mono8")
        yellow_edges = cv2.bitwise_and(edges, yellow_image)
        output_yellow_edges = self.bridge.cv2_to_imgmsg(yellow_edges, "mono8")
        self.pub_yellow.publish(output_yellow_edges)

        white_edges = cv2.bitwise_and(edges, white_image)
        output_white_edges = self.bridge.cv2_to_imgmsg(white_edges, "mono8")
        self.pub_white.publish(output_white_edges)

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
