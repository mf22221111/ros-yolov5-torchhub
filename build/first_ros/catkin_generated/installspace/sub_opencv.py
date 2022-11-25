import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
def ba(img):
    bridge = CvBridge()
    img = bridge.imgmsg_to_cv2(img, desired_encoding="passthrough")

    cv2.imshow('1',img)
    cv2.waitKey(1)


if __name__ == '__main__':

    rospy.init_node('sub_op')

    rospy.Subscriber('yolo_res',Image,ba)

    rospy.spin()