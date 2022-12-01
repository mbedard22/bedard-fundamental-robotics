#!/usr/bin/env python3 

import rospy
import actionlib
import example_action_server.msg
from example_service.srv import Fibonacci

if __name__=="__main__":
    rospy.init_node("hw10_node")
    rate = rospy.Rate(1)
    rate.sleep()
    rospy.loginfo("node initiated")

    rospy.wait_for_service("/calc_fibonacci")
    calc_fib = rospy.ServiceProxy("/calc_fibonacci", Fibonacci)
    
    rospy.loginfo("SERVICE: call calc_fib order 3")
    resp1 = calc_fib(3)
    rospy.loginfo(resp1.sequence)
      
    rospy.loginfo("SERVICE: call calc_fib order 15")
    resp1 = calc_fib(15)
    rospy.loginfo(resp1.sequence)


    client = actionlib.SimpleActionClient('fibonacci', example_action_server.msg.FibonacciAction)
    client.wait_for_server()
    
    goal = example_action_server.msg.FibonacciGoal(order=3)
    client.send_goal(goal)
    client.wait_for_result()
    rospy.loginfo(client.get_result())  # A FibonacciResult

    goal = example_action_server.msg.FibonacciGoal(order=15)
    client.send_goal(goal)
    client.wait_for_result()
    rospy.loginfo(client.get_result())  # A FibonacciResult
