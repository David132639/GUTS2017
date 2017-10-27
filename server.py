import socket
import time
from threading import Thread

def listen():
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind(("127.0.0.1",5555))
	while True:
        	data,addr=s.recvfrom(1024)
        	print(data.decode("UTF-8"))
	s.close

Thread(target=listen).start()

m=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
	m.sendto(bytes("Hello","UTF-8"),("127.0.0.1",5556))
	time.sleep(1)
