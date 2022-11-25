import rospy
from std_msgs.msg import String

def doMsg(msg):
    rospy.loginfo(msg.data)

if __name__ == '__main__':
    
    rospy.init_node('sub')

    sub = rospy.Subscriber('che',String,doMsg,queue_size=10)

    rospy.spin()

    