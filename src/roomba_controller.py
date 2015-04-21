import os, sys, inspect, socket, time, select, math
import re
from threading import Thread

# add path for create library
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
lib_dir = os.path.abspath(os.path.join(src_dir, '../lib/pycreate'))
sys.path.insert(0, lib_dir)

import create
from multiprocessing import Process, Value, Lock, Manager

# the Roomba needs to know the ROS Publisher's IP and Port to connect to
# default is to use localhost

FOR_TURNS = 0.5
FOR_STRAIGHT = 1
STRAIGHT_THRESHOLD = 1.5
PERIOD = FOR_STRAIGHT

def controlled_move(robot, host, port):

	# function to move the robot through continuous input
	# default behavior is the robot moves until new command is given (default behavior of roomba)
	MAX_ANGULAR_VELOCITY = 10
	MAX_LINEAR_VELOCITY = 10
	global PERIOD
	running = True
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(5) 
	# connect to remote host
	try :
		s.connect((host, port))
	except :
		print('Unable to connect')
		sys.exit()

	print('Connected to command host. Start sending messages')
	while running:
		socket_list = [s]
 
		# Get the list sockets which are readable
		read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
		for sock in read_sockets:
			#incoming message from remote server
			if sock == s:
				data = sock.recv(4096)
				data = data.decode() # convert to python 3 strings (Unicode)
				if not data :
					print('\nDisconnected from command server')
					robot.shutdown()
					print("done!")
					sys.exit()
				else :
					#print data
					# handle the data here
					movement_command = str(data)
					#sys.stdout.write(movement_command)
					#sys.stdout.write("\n")
					#sys.stdout.flush()
					movement_command_array = movement_command.split("\n")
					for command in movement_command_array:
						sys.stdout.write(command)
						sys.stdout.write("\n")
						sys.stdout.flush()
					m = re.findall('[A-Za-z]+\:\s(-?[0-9]+.[0-9]+)', movement_command)
					
					if len(m) < 6:
						continue

					linear = float(m[0])
					angular = float(m[5])

					if linear > MAX_LINEAR_VELOCITY: linear = MAX_LINEAR_VELOCITY
					if angular > MAX_ANGULAR_VELOCITY: angular = MAX_ANGULAR_VELOCITY

					if linear < -MAX_LINEAR_VELOCITY: linear = -MAX_LINEAR_VELOCITY
					if angular < -MAX_ANGULAR_VELOCITY: angular = -MAX_ANGULAR_VELOCITY

					sys.stdout.write("regex here\n")

					#sys.stdout.write("previous period is " + str(PERIOD))

					# also control the odometry update period depending on linear/angular
					# assumes that the robot only turns in place or goes straight
					if linear > STRAIGHT_THRESHOLD:
						PERIOD = FOR_STRAIGHT
					elif linear == 0 and angular == 0:
						PERIOD = FOR_STRAIGHT
					else:
						PERIOD = FOR_TURNS
					
					#sys.stdout.write("I think the period is " + str(PERIOD))
					sys.stdout.write("\n")

					'''
					for i in m:
						sys.stdout.write(i)
						sys.stdout.write("\n")
					'''
					sys.stdout.write(str(linear))
					sys.stdout.write("\n")
					sys.stdout.write(str(angular))
					sys.stdout.write("\n")
					sys.stdout.flush()
					# grab the lock and give robot commands
					# assumes command is of the form x:%d, y, z; r, p, y
									
					robot.go(linear, angular)
					

			#user entered a message
			else :
				msg = sys.stdin.readline()
				if msg == "STOP":
					robot.stop()



def send_odometry(robot, odometry_server_name, odometry_server_port):
	# function to periodically send odometry data to a ROS publisher node
	# checks the lock and if not in use, sends distance and angle update

	# period of updates
	global PERIOD
	MAX_STRAIGHT_ENCODER_VALUE = 200
	MAX_ANGLE_ENCODER_VALUE = 30

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(5) 
	# connect to remote host
	try :
		s.connect((odometry_server_name, odometry_server_port))
	except :
		print('Unable to connect')
		sys.exit()
	running = True
	print('Connected to odometry host. Start sending messages')
	try:
		while running:	
			distance = robot.getSensor("DISTANCE")
			angle = robot.getSensor("ANGLE")

			# control unreasonable distance and angle read values
			# set them to 0 and notify the user to restart the program

			if distance > MAX_STRAIGHT_ENCODER_VALUE or angle > MAX_ANGLE_ENCODER_VALUE:
				print("extremely high roomba encoder readings!", distance)
				print("made the robot stop!")
				distance = 0
				angle = 0
				robot.go(0,0)
				robot.shutdown()
				sys.exit()

			if distance is None or angle is None:
				print("failed to get reading from roomba. automatic shutdown")
				robot.shutdown()
				sys.exit()
			
			#distance = 10
			#angle = 10
			msg = str(distance) + ";" + str(angle)
			print(distance)
			print(angle)
			print(msg)
			msg = bytes(msg, 'UTF-8')
			print("sending create odometry to ROS node")
			s.send(msg)
			time.sleep(PERIOD)
			print("actual period is", PERIOD)
	except :
		print("odometry publisher crashed")
		robot.shutdown()
		print("done!")
		sys.exit()


if __name__ == "__main__":
	if (len(sys.argv) != 2):
		print("Need more command line arguments")
		sys.exit(2)

	serPort = int(sys.argv[1])
	'''
	host = sys.argv[2]
	port = sys.argv[3]
	'''
	command_host = "160.39.240.59"	# hostname for component that gives commands
	command_port = 8001             # same port as used by the server

#	r = "hi"
	r = create.Create(serPort)

	distance = r.getSensor("DISTANCE")
	angle = r.getSensor("ANGLE")


	# python multiprocessing
	# wrap the robot with Value for shared memory

	odometry_host = command_host
	odometry_port = 8000
	
	#send_odometry(r, odometry_host, odometry_port)
	#controlled_move(r, command_host, command_port)

	controlled_move_thread = Thread(target=controlled_move, args=(r, command_host, command_port))
	send_odometry_thread = Thread(target=send_odometry, args=(r, odometry_host, odometry_port))
	
	# start the thread
	controlled_move_thread.start()
	send_odometry_thread.start()

	# wait on the threads to terminate
	controlled_move_thread.join()
	send_odometry_thread.join()

