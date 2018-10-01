#!/usr/bin/env python3
import socket

TCP_IP = 'localhost'
TCP_PORT = 37
MESSAGE = "THIS IS THE MESSAGE"

print("UDP target IP:", TCP_IP)
print("UDP target port:", TCP_PORT)
print("Sent:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP,TCP_PORT))
sock.sendto(bytes(MESSAGE, "utf-8"), (TCP_IP, TCP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("Received:")
    print(data)

    print("Socket closing...")
    sock.close()
    quit()