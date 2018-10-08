#!/usr/bin/env python

import socket, time


TCP_IP = '127.0.0.1'
TCP_PORT = 37
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()

epoch_time = int(time.time()) + 2208988800
string_epoch = str(epoch_time)

print ('Connected by', addr)
while 1:
    data = conn.recv(1024)
    if not data: break

    conn.sendall(bytes(string_epoch, "utf-8"))
    print("Message sent: ", string_epoch)
conn.close()