#! /usr/bin/env python
import rospy
rospy.init_node("hello_python_node")
a=5
b=10
c=16
d=int(input('d='))
e=int(input('e='))
if d>a and d<b or e<c:
	print('go')
else:
	print('stop')
