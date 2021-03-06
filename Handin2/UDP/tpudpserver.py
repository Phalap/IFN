#!/usr/bin/env python3

import socket
import time
from struct import pack

UDP_IP = "127.0.0.1"
UDP_PORT = 37

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

while True:

    data, addr = sock.recvfrom(1024)
    print("New client connected")
    print("Received:", data, " From: ", addr)

    epoch_time = int(time.time()) + 2208988800
    string_epoch = str(epoch_time)

    time = pack('I',epoch_time)

    sock.sendto(time, addr)
    print("Server has now responded with time and date to client")

