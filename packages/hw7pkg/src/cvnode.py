#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImageFlippa:
    def __init__(self):
        rospy.Subscriber("image", Image, self.flippa_cb)
        self.pub = rospy.Publisher("flipped", Image, queue_size = 10)

        self.bridge = CvBridge()
    def flippa_cb(self, msg):
        cv_img - self.bridge.imgmsg_to_cv2(msg, "bgr8")

        cv_flipped = cv2.flip(cv_img, 0)

        ros_flipped = self.bridge.cv2_to_imgmsg(cv_flipped, "bgr8")

        self.pub.publish(ros_flipped)

if __name__ == "__main__":
    rospy.init_node("image_flipper", anonymous = True)
    img_flip = ImageFlippa()
    rospy.spin()
