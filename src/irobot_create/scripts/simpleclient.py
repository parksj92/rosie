import socket, time

host = socket.gethostname()    
port = 8000                   # The same port as used by the server
i = 0
while i<10:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	s.sendall(b'Hello, world')
	data = s.recv(1024)
	time.sleep(2)
	print('Received', repr(data))
	i += 1
	s.close()
