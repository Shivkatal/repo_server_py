import socket
commands = ["share","download","exit"]

def download(sock):
	filename = str(raw_input())
	sock.send(filename)
	cnt = 0
	mirrors = {}
	cnt = int(sock.recv(3))

	if cnt == 0:
		print "File not found!!!"
		return
	#print cnt
	for i in range(1,cnt+1):
		sz = int(sock.recv(4))
		mirror = sock.recv(sz)
		print i, mirror
		mirrors[cnt] = mirror


	print "Select Your choice:"
	opt = int(raw_input())
	



#create a socket object
s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get local machine name
host = socket.gethostname()
port = 9998

#connection to hostname on the port
s.connect((host, port))

#receive no more than 1024 bytes
tm = s.recv(1024)

print "The time got from server is %s" % tm.decode('ascii')

while True:
	choice = str(raw_input())
	if choice not in commands or choice == "exit":
		s.send("exit")
		break
	s.send(choice)
	if choice == "share":
		filename = str(raw_input())
		s.send(filename)
		path =  str(raw_input())
		s.send(path)
	elif choice == "download":
		download(s)

s.close()

