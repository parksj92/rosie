import os, sys, inspect, socket, time, select

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
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2) 
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print('Unable to connect')
        sys.exit()

    print('Connected to remote host. Start sending messages')
    while running:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                data = data.decode() # convert to python 3 strings (Unicode)
                if not data :
                    print('\nDisconnected from server')
                    sys.exit()
                else :
                    #print data
                    # handle the data here
                    movement_command = str(data)
                    movement_command_array = movement_command.split(" ")
                    for command in movement_command_array:
                    	sys.stdout.write(command)
             
            #user entered a message
            else :
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()

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
