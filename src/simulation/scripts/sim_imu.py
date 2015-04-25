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
last_time = 0
last_x = 0
last_y = 0
last_z = 0
rots = 0
def imu_publisher():
    global last_r
    global last_p
    global last_yaw
    global last_x
    global last_y
    global last_z
    global last_time
    global rots

    pub = rospy.Publisher('imu_data', sensor_msgs.msg.Imu, queue_size=100)
    rospy.init_node('imu', anonymous=True)
    rate = rospy.Rate(10)

    current_time = rospy.get_rostime()
    last_time = rospy.get_rostime()
    yaw_deg = 0
    #yaw = math.radians(0)
    print "Initial Yaw", yaw_deg

    while not rospy.is_shutdown():
        rots += 1
        current_time = rospy.get_rostime()
        roll    = 0 
        pitch   = 0 
        #yaw_deg     = float(yaw_deg) + float(0.5)
        if rots < 100:
            #yaw     = float(yaw) + float(math.radians(0.5))
            yaw_deg     = float(yaw_deg) + 0.5
        else: 
            #yaw += 0
            yaw_deg += 0
        x       = 0
        y       = 0 
        z       = 0 

        rospy.logwarn("yaw_deg: %f, rots: %f", yaw_deg, rots)

        #rospy.loginfo("Deg: roll %f\t pitch %f\t yaw %f\t", roll, pitch, yaw)
        roll = math.radians(roll)
        pitch = math.radians(pitch)
        yaw = math.radians(yaw_deg) 
        rospy.loginfo("Rad: roll %f\t pitch %f\t yaw %f\t", roll, pitch, yaw)
        
        dt = (current_time - last_time).to_sec()
        quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw) 


        # Publish transform odom -> base_link over tf
        odom_broadcaster = tf.TransformBroadcaster()
        odom_broadcaster.sendTransform((0.0,0.0,0.0), (0,0,0,1), current_time, "imu", "base_link")

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
                                         0, 0, math.pow(0.00017,2)] # 0.01 deg/sec

        rospy.logwarn("yaw:%f, last_yaw:%f, dt: %f", yaw, last_yaw, dt)
        # Angular velocity is in degrees per second (because the IMU gives angles in degrees)
        imu.angular_velocity.x = (float(roll - last_r) /(dt))
        imu.angular_velocity.y = (float(pitch - last_p) /(dt))
        imu.angular_velocity.z = (float(yaw - last_yaw) /(dt))

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

