#!/usr/bin/env python3

import socket

target_host = "127.0.0.1"
target_port = 9998

#create a socket object
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#CONNECT TO THE CLIENT
client.connect((target_host,target_port))

#send some data
client.send('GET / HTTP/1.1\r\nHost: google.com\r\n\r\n'.encode('utf-8'))

#receive some data
response = client.recv(4096)

print(response)