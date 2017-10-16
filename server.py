import socket
import time

#create a socket object
serversocket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get local machine name
host = socket.gethostname()
port = 9999

#bind to the port
serversocket.bind((host, port))

#queue upto 5 requests
serversocket.listen(5)
while True:
	flag=1
	clientsocket, addr =  serversocket.accept()
	print "Got a connection from %s" % str(addr)
	currentTIme = time.ctime(time.time())+"\r\n"
	clientsocket.send(currentTIme.encode('ascii'))
	while flag:
		#establish connection
		choice = clientsocket.recv(10)
		print choice
		if choice != '1':
			flag = 0

	clientsocket.close()