import os, sys, inspect
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
lib_dir = os.path.abspath(os.path.join(src_dir, '../lib/pycreate'))
sys.path.insert(0, lib_dir)

import create


def controlled_move(robot):

	# function to move the robot through continuous input
	# default behavior is the robot moves until new command is given (default behavior of roomba)

	DEFAULT_ANGULAR_VELOCITY = 5
	DEFAULT_LINEAR_VELOCITY = 15
	running = True
	while running:
		movement_command = input("Direction degree: ")
		movement_command_array = movement_command.split(" ")

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



if __name__ == "__main__":
	if (len(sys.argv) != 2):
		print("Need more command line arguments")
		sys.exit(2)

	serPort = int(sys.argv[1])
	r = create.Create(serPort)
	controlled_move(r)


