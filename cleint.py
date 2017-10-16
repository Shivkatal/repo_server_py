import socket

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

choice = str(input())
while choice=='1':
	s.send(choice)
	choice = str(input())

s.close()

