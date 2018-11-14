#!/usr/bin/env python3
import socket
from struct import unpack

UDP_IP = "127.0.0.1"
UDP_PORT = 37
MESSAGE = "THIS IS THE MESSAGE"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("Sent:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    time = unpack("I", data)
    time = time[0]

    print("Received:")

    print(time)

    print("Socket closing...")
    sock.close()
    quit()