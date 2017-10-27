import socket

s=socket.socket()
host=socket.gethostname()
port=5555

s.connect((host,port))
#s.sendall(bytes("Hello","UTF-8"))
print(s.recv(1024))
s.close
