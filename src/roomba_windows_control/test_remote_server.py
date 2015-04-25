import os, sys, inspect, socket, time, select

command_host = "160.39.241.180"	# hostname for component that gives commands
command_port = 8001             # same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2) 
try :
	s.connect((command_host, command_port))
except :
	print('Unable to connect')
	sys.exit()

print("connected to command server")

odometry_host = command_host
odometry_port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2) 
try :
	s.connect((odometry_host, odometry_port))
except :
	print('Unable to connect')
	sys.exit()
print("connected to odometry publisher")