#!/usr/bin/env python

import rospy
import geometry_msgs.msg

def initialpose_publisher():
    
    init_times = 30
    i = 0
    pub = rospy.Publisher('/cmd_vel', geometry_msgs.msg.Twist, queue_size=100)

    rospy.init_node('cancel_goal_publisher', anonymous=True)
    rate = rospy.Rate(100)

    while not rospy.is_shutdown():
        if i == init_times:
            break
        current_time = rospy.get_rostime()
        cancel_goal = geometry_msgs.msg.Twist()

        # got these values from clicking on rviz

        cancel_goal.linear.x = 0.0 
        cancel_goal.linear.y = 0.0 
        cancel_goal.linear.z = 0.0 

        cancel_goal.angular.x = 0.0 
        cancel_goal.angular.y = 0.0 
        cancel_goal.angular.z = 0.0 
                                        
        pub.publish(cancel_goal)
        i+=1
        rospy.logwarn("Published Cancel Goal %d times", i)
        rate.sleep()


if __name__ == '__main__':
    try:
        initialpose_publisher()
    except rospy.ROSInterruptException:
        pass

