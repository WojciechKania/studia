#!/usr/bin/env python
import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "get route table"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
s.connect((TCP_IP, TCP_PORT))  # Connect the socket to the port where the server is listening
s.send(MESSAGE)                # send request
data = s.recv(BUFFER_SIZE)     # receive data
s.close()

print ("received data:", data)
