#!/usr/bin/env python
 
import socket
from struct import unpack

TCP_IP = '127.0.0.1'
TCP_PORT = 37
BUFFER_SIZE = 20
MESSAGE = "Hello from client!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(bytes(MESSAGE, "utf-8"))
data = s.recv(BUFFER_SIZE)
s.close()

time = unpack("I", data)
#Removing junk from the printout
time = time[0]

print("received data: " +  str(time))
