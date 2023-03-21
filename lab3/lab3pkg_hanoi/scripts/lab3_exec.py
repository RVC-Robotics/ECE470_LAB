#!/usr/bin/env python

'''

lab3pkg_hanoi/lab3_exec.py

@brief: Hanoi implementation in ROS.

@author: Songjie Xiao
@date: Monday 2023/1/16

'''

import sys
import time
import numpy as np
import rospy

# IMPORT! headers for ROS messages and include useful message types
from lab3_header import *

# define global variables here
# store the current position of the arm
current_position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
# store the current state of the suction cup
current_io_0 = False

suction_on = True
suction_off = False

############## Your Code Start Here ##############

"""
TODO: define position of our tower in Q array and home position of the arm
"""

home = np.radians([0.00, 0.00, 0.00, 0.00, 0.00, 0.00])

Q = None





############### Your Code End Here ###############
 
 

 
 
############## Your Code Start Here ##############

"""
TODO: define a ROS topic callback function for getting the state of suction cup
Whenever /ur_hardware_interface/io_states publishes info, this callback function is called.
"""
def gripper_input_callback(msg):

	global current_io_0

	pass



 
############## Your Code Start Here ##############

"""
TODO: define a ROS topic callback function for getting the current position of the arm
Whenever /joint_states publishes info, this callback function is called.
"""
def position_callback(msg):

	global current_position
	
	pass



############## Your Code Start Here ##############

"""
TODO: define a function for ROS Publisher to publish your message to the Topic "ur3e_driver_ece470/setio",
so that we can control the state of suction cup.
"""
def gripper(pub_setio, io_0):

	pass
 


############### Your Code End Here ###############

# Function for moving the arm to a desired location
def move_arm(pub_setjoint, dest):
	msg = JointTrajectory()
	msg.joint_names = ["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint","wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]
	point = JointTrajectoryPoint()
	point.positions = dest
	point.time_from_start = rospy.Duration(2)
	msg.points.append(point)
	pub_setjoint.publish(msg)
	time.sleep(2.5)

############## Your Code Start Here ##############
"""
TODO: define move_block function which is used to move a block from start to end location
which includes moving the arm to the start location, gripping the block, moving the arm to the end location, and releasing the block
"""
### Hint: Use the Q array to map out your towers by location and height.

def move_block(pub_setjoint, pub_setio, start_loc, start_height, end_loc, end_height):

	global Q
	
	pass
 
 
 
############### Your Code End Here ###############
 
 
def main():
 
	global home
	global Q

	# Definition of our tower

	# block contact position
	# | Q[0][0] Q[0][1] Q[0][2] |   Contact point of top block
	# | Q[1][0] Q[1][1] Q[1][2] |   Contact point of middle block
	# | Q[2][0] Q[2][1] Q[2][2] |   Contact point of bottom block
	# | Tower1  Tower2  Tower3  |

	# First index - From "top" to "bottom"
	# Second index - From "left" to "right"

	# How the arm will move (Suggestions)
	# 1. Go to the "home" position
	# 2. Drop to the "contact (start) block" position
	# 3. Rise back to the "home" position
	# 4. Drop to the corresponding "contact (end) block" position
	# 5. Rise back to the "home" position

	# Initialize ROS node
	rospy.init_node('lab3_node')
 
	# Initialize publisher for ur3e_driver_ece470/setjoint with buffer size of 10
	pub_setjoint = rospy.Publisher('ur3e_driver_ece470/setjoint', JointTrajectory, queue_size=10)
	
	# TODO: define a ROS publisher for /ur3e_driver_ece470/setio message and corresponding callback function
	# pub_setio = 

	# Initialize subscriber to /joint_states, each time /joint_states publishes a new message, the function position_callback is called
	sub_position = rospy.Subscriber('/joint_states', JointState, position_callback)
 
	# TODO: define a ROS subscriber for /ur_hardware_interface/io_states message and corresponding callback function
	# sub_io = 
 
	############## Your Code Start Here ##############
	# This program will requires two user inputs to specify the start location and end location of the block
	# TODO: modify the code below so that program can get two user inputs
	# example code for getting user input is provided below
	input_done = 0
	start = 0
	mid = 1
	des = 2

	while(not input_done):
		input_string = input("Enter number of loops <Either 1 2 3 or 0 to quit> ")
		print("You entered " + input_string + "\n")

		if(int(input_string) == 1):
			input_done = 1
		elif (int(input_string) == 2):
			input_done = 1
		elif (int(input_string) == 3):
			input_done = 1
		elif (int(input_string) == 0):
			print("Quitting... ")
			sys.exit()
		else:
			print("Please just enter the character 1 2 3 or 0 to quit \n\n")




			

	############### Your Code End Here ###############
 
	rospy.loginfo("Sending Goals ...")
 
	############## Your Code Start Here ##############
	# Main manipulation code defined here
	# move_arm function is used to move the arm to a desired position
	# move_block function is used to move a block from start to end location
	# which includes moving the arm to the start location, gripping the block, moving the arm to the end location, and releasing the block
	# TODO: here to define a series of move_block or move_arm function calls to solve the Hanoi Tower problem
 
	# move_block(pub_setjoint, pub_setio, start, 0, des,   2)


	pass


	
	# move_arm(pub_setjoint, home)
 
	############### Your Code End Here ###############
 
 
 
if __name__ == '__main__':
	try:
		main()
	# When Ctrl+C is executed, it catches the exception
	except rospy.ROSInterruptException:
		pass
