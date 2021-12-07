#! /usr/bin/env python
import rospy
rospy.init_node("hello_python_node")
n=3
d=[]
for i in range(n):
	a=int(input())
	d.append(a)
print(d)
print(sorted(d))

