import socket
import time
from threading import Thread

def listen():
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.bind(("0.0.0.0",5556))
        while True:
                data,addr=s.recvfrom(1024)
                print(data.decode("UTF-8"))
        s.close

list=Thread(target=listen)
list.daemon=True
list.start()

m=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
	msg=raw_input("What?")
	m.sendto(msg,("127.0.0.1",5555))
