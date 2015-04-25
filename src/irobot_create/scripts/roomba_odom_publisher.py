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
import csv

def main():
    # List to keep track of socket descriptors
    CONNECTION_LIST = []
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 8000 # arbitrary port
    MAX_THETA = 30
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = ''
    server_socket.bind((host, PORT))
    server_socket.listen(10)
 
    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)
 
    print ("Roomba Odometry Publisher started on: " + str(PORT))
    rospy.init_node('create_odometry_publisher', anonymous=True) 
    #rate = rospy.Rate(10)


    max_angle_change = 15 # per timestep
    # Max of 72 deg / sec --> 15 deg / 0.2 sec
    max_distance_change = 100 # per timestep

    while 1:
        # Get the list sockets which are ready to be read through select
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
 
        for sock in read_sockets:
            #New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr

            #Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    #In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)
                    print "received odometry data" 
                    if data:
                        #print data
                        m = re.findall('(-?[0-9]+);(-?[0-9]+)', data)
                        #print m[0]
                        if len(m) != 1:
                            continue
                        if len(m[0]) != 2:
                            continue

                        d = float(m[0][0])
                        theta = (float(m[0][1]))
                        if theta > MAX_THETA:
                            theta = 0
                        rospy.loginfo("d and theta are %f and %f", d, theta)
                        # if theta>max_angle_change: theta = max_angle_change
                        # if theta<0: theta = 0
                        # if d>max_distance_change: d = max_distance_change
                        #print d, theta
                        publish_odometry(d, theta)
                        # rate.sleep()
                        # here should put function to do ROS publisher actions

                except:
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
     
    server_socket.close()

gl_x = 0
gl_y = 0
gl_th = 0
gl_then = datetime.now()
odomBroadcaster = TransformBroadcaster()
odomPub = rospy.Publisher('create_odometry',Odometry)

def publish_odometry(d_create, theta_create):
        print "publishing odometry"
        if not rospy.is_shutdown():
            global gl_x
            global gl_y
            global gl_th
            global gl_then
            global odomBroadcaster 
            now = datetime.now()
            elapsed = now - gl_then
            gl_then = now
    
            elapsed = float(elapsed.seconds) + elapsed.microseconds/1000000.
            # The create sends distance measurements in mm/sec. We need to convert to m/sec by multiplying by 1000
            d = d_create / 1000 # Check units being sent
            th = radians(theta_create) 

            dx = d / elapsed
            dth = th / elapsed
            
            if (d != 0):
                x = cos(th)*d
                y = -sin(th)*d
                gl_x = gl_x + (cos(gl_th)*x - sin(gl_th)*y)
                gl_y = gl_y + (sin(gl_th)*x + cos(gl_th)*y)

            if (th != 0):
                gl_th = gl_th + th

            quaternion = Quaternion()
            quaternion.x = 0.0 
            quaternion.y = 0.0
            quaternion.z = sin(gl_th/2)
            quaternion.w = cos(gl_th/2)

            rospy.logwarn("elapsed: %f, gl_x: %f, gl_y: %f, gl_th: %f, dth: %f", elapsed, gl_x, gl_y, gl_th, dth)
            odomBroadcaster.sendTransform(
                (gl_x, gl_y, 0), 
                (quaternion.x, quaternion.y, quaternion.z, quaternion.w),
                rospy.Time.now(),
                "base_link",
                "odom"
                )

            with open('../odom_log.csv', 'a',) as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow([d])

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


if __name__ == "__main__":
    main()
