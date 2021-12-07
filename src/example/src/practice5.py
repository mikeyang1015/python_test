#! /usr/bin/env python
import rospy
rospy.init_node("hello_python_node")
for i in range(1,10):
	for j in range(1,10):
		if j==9:
			print('%d*%d=%2ld'%(i,j,i*j))
		else:
			print('%d*%d=%2ld'%(i,j,i*j),end=" ")

