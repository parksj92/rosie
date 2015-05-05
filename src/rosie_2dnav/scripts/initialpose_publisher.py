#!/usr/bin/env python

import rospy
import geometry_msgs.msg

def initialpose_publisher():
    
    init_times = 15
    i = 0
    pub = rospy.Publisher('initialpose', geometry_msgs.msg.PoseWithCovarianceStamped, queue_size=100)

    rospy.init_node('initialpose_publisher', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        if i == init_times:
            break
        current_time = rospy.get_rostime()
        initialpose = geometry_msgs.msg.PoseWithCovarianceStamped()

        initialpose.header.stamp = current_time

        # got these values from clicking on rviz

        initialpose.pose.pose.position.x = 6.83541727066
        initialpose.pose.pose.position.y = 0.639947891235
        initialpose.pose.pose.position.z = 0

        initialpose.pose.pose.orientation.x = 0
        initialpose.pose.pose.orientation.y = 0
        initialpose.pose.pose.orientation.z = -0.998428836684
        initialpose.pose.pose.orientation.w = 0.0560344365342

        initialpose.pose.covariance = [0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 
                                        0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 
                                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                                        0.0, 0.0, 0.0, 0.0, 0.0, 0.06853891945200942]
                                        
        pub.publish(initialpose)
        i+=1
        rospy.logwarn("Published Initial Pose %d times", i)
        rate.sleep()


if __name__ == '__main__':
    try:
        initialpose_publisher()
    except rospy.ROSInterruptException:
        pass

