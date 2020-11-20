#!/usr/bin/env python
import rospy
from common_msg.msg import hw3_msg

def callback(hw3_msg):
    respone = CompareTwoNum(compare = bool(request.a < request.b))
    print "subscribe:", request(hw3_msg.compare = bool(hw3_msg.a < hw3_msg.b))
    return respone

rospy.init_node('hw3_subscriber')
sub = rospy.Subscriber('common_msg', hw3_msg, callback)
rospy.spin()