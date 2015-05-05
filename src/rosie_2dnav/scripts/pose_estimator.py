#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
import geometry_msgs.msg
import numpy

updated_position = False

if __name__ == '__main__':
    rospy.init_node('position_estimator')

    listener = tf.TransformListener()

    initialpose_publisher = rospy.Publisher('/initialpose', geometry_msgs.msg.PoseWithCovarianceStamped,queue_size=1)

    rate = rospy.Rate(10.0)
    #http://answers.ros.org/question/133331/multiply-two-tf-transforms-converted-to-4x4-matrices-in-python/
    while not rospy.is_shutdown():# and updated_position is False:
        try:
            #rospy.logwarn("Trying to find marker")
            (trans1,rot1) = listener.lookupTransform('/marker', '/map', rospy.Time(0))
            trans1_mat = tf.transformations.translation_matrix(trans1)
            rot1_mat   = tf.transformations.quaternion_matrix(rot1)
            mat1 = numpy.dot(trans1_mat, rot1_mat)
            print "Found map -> marker"

            (trans2,rot2) = listener.lookupTransform('/camera', '/marker', rospy.Time(0))
            rospy.logwarn("Found Camera to Marker Transformation")

            trans2_mat = tf.transformations.translation_matrix(trans2)
            rot2_mat = tf.transformations.quaternion_matrix(rot2)
            mat2 = numpy.dot(trans2_mat, rot2_mat)
            
            mat3 = numpy.dot(mat1, mat2)
            trans3 = tf.transformations.translation_from_matrix(mat3)
            rot3 = tf.transformations.quaternion_from_matrix(mat3)
            """
            # Rotate 90 degrees
            euler_rot1 = tf.transformations.euler_from_quaternion(rot1)
            new_yaw = euler_rot1[2]# + float(3.1415/2)
            rot1 = tf.transformations.quaternion_from_euler(euler_rot1[0], euler_rot1[1], new_yaw)
            print "rot1 after 90 rot", rot1
            """
            # initialpose is a transformation from map to base_link
            # T(map -> base_link) = T(map -> marker) * T(marker->camera)
            initialpose = geometry_msgs.msg.PoseWithCovarianceStamped()
            initialpose.header.stamp = rospy.Time.now()
            initialpose.header.frame_id = "map"

            initialpose.pose.pose.position.x = trans3[0]
            initialpose.pose.pose.position.y = trans3[1]
            initialpose.pose.pose.position.z = trans3[2]

            initialpose.pose.pose.orientation.x = rot3[0]
            initialpose.pose.pose.orientation.y = rot3[1]
            initialpose.pose.pose.orientation.z = rot3[2]
            initialpose.pose.pose.orientation.w = rot3[3]

            initialpose_publisher.publish(initialpose)
            print initialpose
            print "Published initialpose"
            updated_position = True

            rate.sleep()
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        """
        br = tf.TransformBroadcaster()
        br.sendTransform(
            trans3,
            rot3,
            rospy.Time.now(),
            "target",
            "source");
        """
