#!/usr/bin/env python

import rospy
import math

from std_msgs.msg import Float64

    

def set_angles(q1, q2):
    rate = rospy.Rate(10)
    i=0
    while (rospy.is_shutdown()!=1):
        pub1.publish(q1)
        pub2.publish(q2)
        rate.sleep()
        i=i+1


def control():
    rospy.init_node('control_test', anonymous=True)
    global pub1, pub2
    pub1=rospy.Publisher('/manipulator/joint1_position_controller/command', Float64, queue_size=10) # joint_1 publisher
    pub2=rospy.Publisher('/manipulator/joint2_position_controller/command', Float64, queue_size=10) # joint_2 publisher
    set_angles(0, 0) 



if __name__ == '__main__':
    try:

        control()
        
    except rospy.ROSInterruptException:
        pass