#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3
from common_msg.msg import hw3

rospy.init_node('hw3_publisher')
requester = rospy.Publisher('common_msg', hw3_msg)
msg = hw3_msg()
rate = rospy.Rate(1)
  
count = 0
compare_num = 20

while count < compare_num
    srand((unsigned int)time(NULL))
    value = rand() % 101 
    if value < compare_num
        req = hw3(a=value, b=compare_num)
        res = requester(req)
    rate.sleep()
    count += 1


