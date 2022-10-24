#!/usr/bin/env python
#ark client source code

import socket

host = 'localhost'
port = 33334

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
print ("Connected to port {}".format(port))
data = input(">>")
sock.sendall(bytes(data, "utf-8"))
data1 = sock.recv(1024)
print ("Recieved {}".format(data1))

sock.close()
