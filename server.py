#!/usr/bin/env python
#ark server source code

import socket

port = 33333
host = 'localhost'

sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen()
c, addr = sock.accept()
data = c.recv(1024)
print ("Recieved {}".format(data))
data = data.upper()
c.sendall(bytes(data))
print ('Sent {}'.format(data))
c.close()
