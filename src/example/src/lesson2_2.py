#! /usr/bin/env python
import rospy
import random
rospy.init_node("hello_python_node")
n=3
num=[[[0 for i in range(n)]for j in range(n)]for k in range(n)]
for i in range(n):
	for j in range(n):
		for k in range(n):
			num[i][j][k]=random.randint(0,255)
print(num)
for i in range(n):
	for j in range(n):
		for k in range(n):
			if num[i][j][k]<125:
				num[i][j][k]=0
			else:
				num[i][j][k]=1
print(num)
