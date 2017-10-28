import Tkinter
import time
import socket
from threading import Thread

m=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
def listen():
    r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    r.bind(("0.0.0.0",5555))
    while True:
            data,addr=r.recvfrom(1024)
            keypress_foreign(data)
    r.close

list=Thread(target=listen)
list.daemon=True
list.start()

tk=Tkinter.Tk()

def keypress_local(event):
    print "Local:",repr(event.keysym)
    m.sendto(event.keysym,("127.0.0.1",5556))

def keypress_foreign(data):
    print "Foreign:",repr(data)

tk.bind("<Key>",keypress_local)    

while True:
    time.sleep(0.001)
    tk.update_idletasks()
    tk.update()

