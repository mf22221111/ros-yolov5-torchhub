import torch
import cv2 
import rospy
from sensor_msgs.msg import Image
import sys
import numpy as np
from cv_bridge import CvBridge
from std_msgs.msg import Header
sys.path.insert(0, 'src/first_ros/scripts/yolo')
# Model
model = torch.hub.load('', 'custom',  source='local')  # local repo





# imgs = './data/images/bus.jpg'
IMAGE_WIDTH=1241
IMAGE_HEIGHT=376

# cap = cv2.VideoCapture(0)
# while 1:
#     ret,frame = cap.read()
# def pub_img(img):
#     image_temp=Image()
#     header = Header(stamp=rospy.Time.now())
#     header.frame_id = 'map'
#     image_temp.height=IMAGE_HEIGHT
#     image_temp.width=IMAGE_WIDTH
#     image_temp.encoding='rgb8'
#     image_temp.data=np.array(img).tostring()
#     #print(imgdata)
#     #image_temp.is_bigendian=True
#     image_temp.header=header
#     image_temp.step=1241*3
#     img_pub.publish(image_temp)



def yolo(img):

    bridge = CvBridge()
    img = bridge.imgmsg_to_cv2(img, desired_encoding="passthrough")
# Inference
    results = model(img)
    results.save('img_temp')

    # img_np = np.fromfile("D:\矿山\Koala.jpg", dtype = np.uint8)   # 用numpy读取处理图片
    # img = cv2.imdecode(img_np, -1)   # 再对numpy的读取的图片进行转码，转化为图片对象
    img = cv2.imread('img_temp/image0.jpg')
    img = bridge.cv2_to_imgmsg(img, encoding="bgr8")
    #results.show()  # or .show(), .save()
    #pub_img(img)
    img_pub.publish(img)
    # cv2.imshow('YOLOV5', img)
    # cv2.waitKey(1)

    


if __name__ == '__main__':

    rospy.init_node('yolo_ros')

    rospy.Subscriber("/usb_cam/image_raw",Image,yolo,queue_size=1)

    img_pub = rospy.Publisher('yolo_res',Image,queue_size=1)

    rospy.spin()