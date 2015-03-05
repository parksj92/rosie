import os, sys, inspect, socket, time

# add path for create library
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
lib_dir = os.path.abspath(os.path.join(src_dir, '../lib/pycreate'))
sys.path.insert(0, lib_dir)

import create

# the Roomba needs to know the ROS Publisher's IP and Port to connect to
# default is to use localhost


def controlled_move(robot, host, port):

	# function to move the robot through continuous input
	# default behavior is the robot moves until new command is given (default behavior of roomba)

	DEFAULT_ANGULAR_VELOCITY = 5
	DEFAULT_LINEAR_VELOCITY = 15
	running = True

	while running:
		time.sleep(2)
		# receive command from ROS Publisher via socket
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		data = s.recv(1024) # socket sends binary string
		data = data.decode() # need to convert to python strings
		# parse the data
		# assumes data is of the form: Distance: %d Degree: %d
		movement_command = str(data)
		movement_command_array = movement_command.split(" ")
		for command in movement_command_array:
			print(command)

'''
		# if only direction given, stop the robot
		if len(movement_command_array) == 1:
			robot.stop()

			single_command = movement_command_array[0]
			print(single_command)
			if single_command == "quit":
				robot.shutdown()
				running = False


		else:
			print("Now moving!")
			direction = movement_command_array[0]
			degree = int(movement_command_array[1])

			# directions corresponding to degrees
			# setup with notion forward is 0 degree
			direction_map = {'forward': 0, 'left': 90, 'right': -90, 'backward':180}

			# find the total angle
			total_degree = direction_map[direction] + degree

			# have the robot move in that direction
			# turn first
			print(total_degree)
			print(direction)
			print(degree)
			robot.go(0, DEFAULT_ANGULAR_VELOCITY)
			robot.waitAngle(total_degree)

			# then move forward in that direction
			robot.go(DEFAULT_LINEAR_VELOCITY, 0)
'''

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		print("Need more command line arguments")
		sys.exit(2)

	serPort = int(sys.argv[1])
	'''
	host = sys.argv[2]
	port = sys.argv[3]
	'''
	host = socket.gethostname()    
	port = 8000                   # The same port as used by the server

	r = "hi"
#	r = create.Create(serPort)
	controlled_move(r, host, port)
