#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
import serial
import tf

last_r = 0
last_p = 0
last_y = 0

last_x = 0
last_y = 0
last_z = 0

def imu_publisher():
    global last_r
    global last_p
    global last_y
    global last_x
    global last_y
    global last_z

    pub = rospy.Publisher('imu_data', Imu, queue_size=100)
    rospy.init_node('imu', anonymous=True)
    rate = rospy.Rate(10)
    #port = rospy.get_param('/imu_port', "/dev/ttyACM0")
     
    ser = serial.Serial('/dev/ttyACM0', 115200)
    while True:
        imu_string = ser.readline()
        print imu_string

        # """
        # var = ["Roll", "Pitch", "Heading", "X", "Y", "Z"]
        # output = []

        # for i in range(len(var)):
        #   if(i != len(var)-1):
        #       sub = string[string.find(var[i]) : string.find(var[i+1])-1]
        #       subarray = sub.split(" ")
        #       subarray[1] = float(subarray[1][0:len(subarray[1])-2])
        #       output.append(subarray)
        #   else:
        #       sub = string[string.find(var[i]) :]
        #       subarray = sub.split(" ")
        #       subarray[1] = float(subarray[1])
        #       output.append(subarray)

        # print output
        # """

    
    """
    while not rospy.is_shutdown():
        roll = 100
        pitch = 200
        yaw = 60
        x = 10
        y = 10
        z = 10
        # imu_msg = sensor_msgs.msg.Imu()
        # current_time = rospy.get_rostime()
        # imu.header.stamp = current_time
        # imu.header.frame_id = "imu"
        
        quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
        print quaternion
   


        # TODO
        # Quaternion
        imu.orientation.x = quaternion[0]
        imu.orientation.y = quaternion[1]
        imu.orientation.z = quaternion[2]
        imu.orientation.w = quaternion[3]

        imu.orientation_covariance =    [10e-3, 0, 0
                                         0, 10e-3, 0
                                         0, 0, 10e-3]

        imu.angular_velocity.x = 
        imu.angular_velocity.y = 
        imu.angular_velocity.z = 

        imu.linear_acceleration.x = 
        imu.linear_acceleration.y = 
        imu.linear_acceleration.z = 

        imu.linear_acceleration_covariance = [9]

       

        data = ser.readline()
        """

        # pub.publish()
        rate.sleep()

if __name__ == '__main__':
    try:
        imu_publisher()
    except rospy.ROSInterruptException:
        pass    



