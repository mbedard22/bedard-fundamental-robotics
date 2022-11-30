#!/usr/bin/env python3 

import rospy
from example_service.srv import *

def fib_client(x):
    rospy.wait_for_service('calc_fibonacci')
    try:
        calc_fibonacci = rospy.ServiceProxy('calc_fibonacci', Fibonacci)
        resp1 = calc_fibonacci(x)
        return resp1.sequence
    except (rospy.ServiceException) as e:
        print("Service call failed: %s" %e)

if __name__=="__main__":
    print fib_client(3)
    print fib_client(15)
