#!/usr/bin/env python

import socket, time
import rospy
from geometry_msgs.msg import Twist

"""
This file listens to the teleop commands from /cmd_vel topic, and sends them via topic to the mvt_msg_server
"""

# add path for create library
#src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
#lib_dir = os.path.abspath(os.path.join(src_dir, '../lib/pycreate'))
#sys.path.insert(0, lib_dir)

#import create

host = socket.gethostname()    
port = 8001                   # The same port as used by the server

# receive command from ROS Publisher via socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
	
def callback(data):
    print data.linear
    print data.angular
    global s
    global host
    global port
    
    data_str = str(data.linear) + "\n" + str(data.angular)
    print data_str
    #data = bytes(data_str, 'UTF-8')
    confirmation = s.send(data_str) # socket sends binary string
    print confirmation
    #s.close()
   
def listener():
    rospy.init_node("cmd_listener", anonymous=True)
    rospy.Subscriber("/cmd_vel", Twist, callback)

    rospy.spin()

# the Roomba needs to know the ROS Publisher's IP and Port to connect to
# default is to use localhost

if __name__ == "__main__":
    listener()
