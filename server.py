import socket
import time

def share(sock, ip):
	filename = sock.recv(100)
	path = sock.recv(1024)
	info = str(ip[0])+' '+filename+' '+path+'\n'
	f = open('repo.txt','a')
	f.write(info)
	f.close()

def findMirrors(file):
	f = open('repo.txt','rb')
	mirrors = {}
	cnt = 0
	for entry in f:
		filename = (entry.split())[1]
		if filename == file:
			mirrors[cnt] = entry
			cnt += 1
	f.close()
	return mirrors, str(cnt)

def downloadServer(csock):
	file = csock.recv(100)
	mirrors, cnt = findMirrors(file)	#find the list of files with details
	if len(cnt) == 1:
		cnt = "00"+cnt
	elif len(cnt) == 2:
		cnt = "0"+cnt
	csock.send(cnt)				#making ensure that size of buffer is full
	cnt = int(cnt)
	for i in range(0,cnt):
		sz = str(len(mirrors[i]))		#sending the length of data before sending the data
		while len(sz) < 4:
			sz = "0"+sz
		#print sz,i
		csock.send(sz)
		csock.send(mirrors[i])
	opt = csock.recv(4)
	opt = int(opt)-1
	if opt < 0:
		return
	details = mirrors[opt].split()
	path = details[2]+details[1]
	print path
	read_file = open(path, 'rb')
	packet = ""
	for data in read_file:
		packet += data
		if len(packet) >= 1024:
			csock.send("1024")
			csock.send(packet[:1024])
			packet = packet[1024:]
	length = str(len(packet))
	while len(length) < 4:
		length = "0"+length

	csock.send(length)
	csock.send(packet)
	csock.send("0000")

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
		elif choice == "download":
			downloadServer(clientsocket)
			

	clientsocket.close()


