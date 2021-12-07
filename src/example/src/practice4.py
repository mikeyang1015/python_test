#! /usr/bin/env python
import rospy
rospy.init_node("hello_python_node")
for i in range(1,5):
	print('*'*i)
