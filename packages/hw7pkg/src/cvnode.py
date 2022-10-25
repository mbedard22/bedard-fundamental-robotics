#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImageCropper:
    def __init__(self):
        rospy.Subscriber("/image", Image, self.cropper_cb)

        self.pub = rospy.Publisher("/image_cropped", Image, queue_size = 10)
        self.pub_white = rospy.Publisher("/image_white", Image, queue_size = 10)
        self.pub_yellow = rospy.Publisher("/image_yellow", Image, queue_size = 10)
        self.bridge = CvBridge()

    def cropper_cb(self, msg):
        cv_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        cv_cropped = cv_img[240:480,0:640]
        ros_cropped = self.bridge.cv2_to_imgmsg(cv_cropped, "bgr8")
        self.pub.publish(ros_cropped)
        
        image_hsv = cv2.cvtColor(cv_cropped, cv2.COLOR_BGR2HSV)
        image_white = cv2.inRange(image_hsv,(30,0,155),(255,100,255))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        white_erode = cv2.erode(image_white, kernel)
        white_dilate = cv2.dilate(white_erode, kernel)
        output_white = self.bridge.cv2_to_imgmsg(white_dilate, "mono8")
        self.pub_white.publish(output_white)

        image_yellow = cv2.inRange(image_hsv,(25,100,100),(50,255,255))
        yellow_erode = cv2.erode(image_yellow, kernel)
        yellow_dilate = cv2.dilate(yellow_erode, kernel)
        ros_yellow = self.bridge.cv2_to_imgmsg(yellow_dilate, "mono8")
        self.pub_yellow.publish(ros_yellow)

if __name__ == "__main__":
    rospy.init_node("image_cropper", anonymous = True)
    img_crop = ImageCropper()
    rospy.spin()
