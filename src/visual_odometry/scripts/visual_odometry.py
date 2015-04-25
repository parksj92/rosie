#!/usr/bin/env python
import roslib
roslib.load_manifest('visual_odometry')
import rospy
import math
import tf
import nav_msgs.msg 
import geometry_msgs
import turtlesim.srv

# initial positions
last_x = 0 
last_y = 0
last_z = 0
last_theta = 0

def visual_odometer():
    # Act on global variables
    global last_x
    global last_y 
    global last_z
    global last_theta

    # topic published
    odom_pub = rospy.Publisher('vo', nav_msgs.msg.Odometry, queue_size=50)
    # initialize node
    rospy.init_node('visual_odometer', anonymous=True)
    r = rospy.Rate(10.0)
    # listen to marker - camera transform (robot position from visual odometry)
    listener = tf.TransformListener()
    # declare broadcaster
    
    odom_broadcaster = tf.TransformBroadcaster()
    current_time = rospy.get_rostime()
    last_time = rospy.get_rostime()

    while not rospy.is_shutdown():
        #rospy.spin()
        current_time = rospy.get_rostime()
        dt = (current_time - last_time).to_sec()
        
        try:
            # robot translation and rotation
            (trans,rot) = listener.lookupTransform('/camera', '/marker', rospy.Time(0))
            #print len(rot)
            #print len(trans)
            vx = (trans[0] - last_x) / dt
            vy = (trans[1] - last_y) / dt
            vz = (trans[2] - last_z) / dt

            rpy = tf.transformations.euler_from_quaternion(rot, 'rxyz') 
            vtheta = (rot[2] - last_theta) / dt

            """
            odom_trans = geometry_msgs.msg.TransformStamped()
            odom_trans.header.stamp = current_time
            odom_trans.header.frame_id = "camera"
            odom_trans.header.child_frame_id = "marker"

            odom_trans.transform.translation.x = x
            odom_trans.transform.translation.y = y
            odom_trans.transform.translation.z = z

            odom_quat = tf.createQuaternionMsgFromYaw(rot(3))
            odom_trans.transform.rotation = odom_quat

            # send the transform
            odom_broadcaster.sendTransform(odom_trans)
            """

            # publish odometry message over ROS
            odom = nav_msgs.msg.Odometry()
            odom.header.stamp = current_time
            odom.header.frame_id = "camera"
            odom.child_frame_id = "marker"

            # set position point
            odom.pose.pose.position.x = trans[0]
            odom.pose.pose.position.y = trans[1]
            odom.pose.pose.position.z = trans[2] 
            # set position quaternion
            odom.pose.pose.orientation.x = rot[0]
            odom.pose.pose.orientation.y = rot[1]
            odom.pose.pose.orientation.z = rot[2]
            odom.pose.pose.orientation.w = rot[3]
            
            # set position covariance
            # Only trust x,y,z and yaw
            odom.pose.covariance = [10e-2, 0, 0, 0, 0, 0, 
                                    0, 10e-2, 0, 0, 0, 0,
                                    0, 0, 10e-2, 0, 0, 0,
                                    0, 0, 0, 10e6, 0, 0,
                                    0, 0, 0, 0, 10e6, 0, 
                                    0, 0, 0, 0, 0, 10e-3]
            

            # set velocity
            odom.twist.twist.linear.x = vx
            odom.twist.twist.linear.y = vy
            odom.twist.twist.linear.z = vz
            #odom.twist.twist.angular.z = vtheta
            
            # set velocity covariance
            #odom.twist.covariance = [36]
            #print odom_trans
             
            last_x = trans[0]
            last_y = trans[1]
            last_z = trans[2]
            last_theta = rot[2]

            odom_pub.publish(odom)
            last_time = current_time
            r.sleep()

        ##odom_broadcaster.sendTransform(
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        
if __name__ == '__main__':
    try:
        visual_odometer()
    except rospy.ROSInterruptException:
        pass

