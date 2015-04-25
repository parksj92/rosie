#!/usr/bin/python
import rospy
import socket, select, re
from time import sleep
from geometry_msgs.msg import Quaternion
from nav_msgs.msg import Odometry
from tf.broadcaster import TransformBroadcaster
from geometry_msgs.msg import Twist
from datetime import datetime
from math import sin,cos,pi, radians

def main():
    global gl_x
    global gl_y
    global gl_th
    global gl_then
   
    rospy.init_node("create_odometry_publisher", anonymous=True)
    #rospy.logwarn("Init vals gl_x %f, g_y %f", gl_x, gl_y)

    while not rospy.is_shutdown():
        now = datetime.now()
        elapsed = now - gl_then
        gl_then = now
        elapsed = float(elapsed.seconds) + elapsed.microseconds/1000000.

        d_create = 1 # 10 mm/sec
        #rospy.logwarn("d_create:%f", d_create)
        theta_create = 0 # 1 deg/sec

        d = float(d_create) / 1000 # Check units being sent
        th = radians(theta_create) 
        #rospy.logwarn("d:%f", d)
        dx = d / elapsed
        dth = th / elapsed
        if (d != 0):
            x = cos(th)*d
            y = -sin(th)*d
            #rospy.logwarn("x:%f, y:%f", x, y)
            gl_x = gl_x + (cos(gl_th)*x - sin(gl_th)*y)
            gl_y = gl_y + (sin(gl_th)*x + cos(gl_th)*y)

        if (th != 0):
            gl_th = gl_th + th

        rate = rospy.Rate(10)
        rospy.loginfo("Roomba Odometry Publisher Simulation Started")

        odomBroadcaster = TransformBroadcaster()
        odomPub = rospy.Publisher('create_odometry',Odometry)

        quaternion = Quaternion()
        quaternion.x = 0.0 
        quaternion.y = 0.0
        quaternion.z = sin(gl_th/2)
        quaternion.w = cos(gl_th/2)

        """
        odomBroadcaster.sendTransform(
                (gl_x, gl_y, 0), 
                (quaternion.x, quaternion.y, quaternion.z, quaternion.w),
                rospy.Time.now(),
                "base_link",
                "map"
                )
                """
        rospy.loginfo("gl_x %f, gl_y %f", gl_x, gl_y)

        odom = Odometry()
        odom.header.stamp = rospy.Time.now()
        odom.header.frame_id = "odom"
        odom.pose.pose.position.x = gl_x
        odom.pose.pose.position.y = gl_y
        odom.pose.pose.position.z = 0
        odom.pose.pose.orientation = quaternion
        
        odom.pose.covariance = [1e-3, 0, 0, 0, 0, 0,
                                     0, 1e-3, 0, 0, 0, 0,
                                     0, 0, 1e6, 0, 0, 0, 
                                     0, 0, 0, 1e6, 0, 0, 
                                     0, 0, 0, 0, 1e6, 0,
                                     0, 0, 0, 0, 0, 1e3 ]

        odom.child_frame_id = "base_link"
        odom.twist.twist.linear.x = dx
        odom.twist.twist.linear.y = 0
        odom.twist.twist.angular.z = dth

        odom.twist.covariance = [1e-3, 0, 0, 0, 0, 0,
                                 0, 1e-3, 0, 0, 0, 0,
                                 0, 0, 1e6, 0, 0, 0, 
                                 0, 0, 0, 1e6, 0, 0, 
                                 0, 0, 0, 0, 1e6, 0,
                                 0, 0, 0, 0, 0, 1e3 ]

        odomPub.publish(odom)
        rate.sleep()

if __name__ == "__main__":
    gl_x = 0
    gl_y = 0
    gl_th = 0
    gl_then = datetime.now()

    main()
