import rospy
from std_msgs.msg import String

# if '__main__' == '__name__':
if __name__ == '__main__':
    
    rospy.init_node('san')

    pub = rospy.Publisher('che',String,queue_size=10)

    msg = String()

    while not rospy.is_shutdown():

        msg.data = 'hello'

        pub.publish(msg)