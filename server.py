import socket
import time

def share(sock, ip):
	filename = sock.recv(100)
	path = sock.recv(1024)
	info = str(ip[0])+' '+filename+' '+path+'\n'
	f = open('repo.txt','a')
	f.write(info)
	f.close()

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
	while True:
		#establish connection
		choice = clientsocket.recv(20)
		print choice
		if choice == "exit":
			break
		if choice =="share":
			share(clientsocket, addr)

	clientsocket.close()


