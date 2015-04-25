#!/usr/bin/env python

import rospy
import sensor_msgs.msg 
import serial
import tf
import re
import signal
import sys
import math

last_r = 0
last_p = 0
last_yaw = 0

last_x = 0
last_y = 0
last_z = 0

def imu_publisher():
    global last_r
    global last_p
    global last_yaw
    global last_x
    global last_y
    global last_z

    pub = rospy.Publisher('imu_data', sensor_msgs.msg.Imu, queue_size=100)
    rospy.init_node('imu', anonymous=True)
    rate = rospy.Rate(10)

    ser = serial.Serial('/dev/ttyACM0', 115200)

    if ser.isOpen():
        rospy.loginfo("Serial port successfully opened")


    current_time = rospy.get_rostime()
    last_time = rospy.get_rostime()

    while not rospy.is_shutdown():
        imu_raw = ser.readline()
        if len(imu_raw) <= 0
           rospy.logwarn("no imu raw data") 
             
        current_time = rospy.get_rostime()
        m = re.findall("[A-Za-z]+:\s(-?[0-9]+.[0-9]+);", imu_raw)

        # Angles in degrees
        if len(m) < 6:
            print "IMU Data hasn't arrived yet"
            continue
        roll    = float(m[0])
        pitch   = float(m[1])
        yaw     = float(m[2])
        x       = float(m[3])
        y       = float(m[4])
        z       = float(m[5])

        rospy.loginfo("Deg: roll %d\t pitch %d\t yaw %d\t", roll, pitch, yaw) 
        # Convert angles to rad
        roll = roll * (-math.pi/180)
        pitch = pitch * (-math.pi/180)
        yaw = yaw * (-math.pi/180)

        rospy.loginfo("Rad: roll %d\t pitch %d\t yaw %d\t", roll, pitch, yaw) 

        dt = (current_time - last_time).to_sec()
        # tf.transformations takes angles in radians (http://www.lfd.uci.edu/~gohlke/code/transformations.py.html)
        quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw) 

        #for i in range(4):
            #quaternion[i] = round(quaternion[i], 2)

        #rospy.loginfo("quaternion[0] %f", quaternion[0])

        # Publish transform odom -> base_link over tf
        odom_broadcaster = tf.TransformBroadcaster()
        # IMU translations attached to odometric frame
        #odom_broadcaster.sendTransform((0.0,0.0,0.0), quaternion, current_time, "imu", "base_link")
        odom_broadcaster.sendTransform((0.0,0.0,0.0), (0,0,0,1), current_time, "imu", "base_link")
        #odom_broadcaster.sendTransform((0.0,0.0,0.0), quaternion, current_time, "imu", "base_link")

        imu = sensor_msgs.msg.Imu()
        imu.header.stamp = current_time
        imu.header.frame_id = "imu"
   
        # Quaternion
        imu.orientation.x = quaternion[0]
        imu.orientation.y = quaternion[1]
        imu.orientation.z = quaternion[2]
        imu.orientation.w = quaternion[3]
        
        # For orientation covariance, 10e3 for pitch and roll, 10e-3 for yaw 
        # So that EKF only considers yaw
        imu.orientation_covariance =    [10e3, 0, 0,
                                         0, 10e3, 0,
                                         0, 0, 10e-3 ]

        print "roll", roll, "last_r", last_r
        print "pitch", roll, "last_p", last_p
        print "yaw", yaw, "last_yaw", last_yaw
        print "dt", dt
        # Angular velocity in rad/sec
        imu.angular_velocity.x = ((roll - last_r) /(dt))
        imu.angular_velocity.y = ((pitch - last_p) /(dt))
        imu.angular_velocity.z = ((yaw - last_yaw) /(dt))

        rospy.loginfo("Angular vels x %f\t y %f\t z %f\t", imu.angular_velocity.x, imu.angular_velocity.y, imu.angular_velocity.z) 

        imu.linear_acceleration.x = x#(x - last_x) / dt
        imu.linear_acceleration.y = y#(y - last_y) / dt
        imu.linear_acceleration.z = z#(z - last_z) / dt

        # For linear acceleration covariances, give large values for EKF to ignore
        imu.linear_acceleration_covariance = [  10e5, 0, 0,
                                                0, 10e5, 0,
                                                0, 0, 10e5 ]
        pub.publish(imu)
        
        last_time = current_time
        last_r = roll
        last_p = pitch
        last_yaw = yaw
        last_x = x
        last_y = y
        last_z = z
    
        rate.sleep()

if __name__ == '__main__':
    try:
        imu_publisher()
    except rospy.ROSInterruptException:
        pass    

