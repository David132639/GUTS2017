import socket

s=socket.socket()
host=socket.gethostname()
port=5555
s.bind((host,port))

s.listen(5)

while True:
	c,addr=s.accept()
	print(addr)
	#m=s.recv(4096)
	c.sendall(bytes("QWERTY",'UTF-8'))
	c.close()
