import socket
commands = ["share","download","exit"]
#create a socket object
s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get local machine name
host = socket.gethostname()
port = 9999

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
s.close()

