"""
Uses sockets for sending data to server and receiving it's answers
"""
import sys, pickle
from socket import *
serverHost = 'localhost'
serverPort = 50007

#message = pickle.dumps('Hello world')

message = [b'Hello network world']  # use only bytes type or str.encode()

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

sockobj = socket(AF_INET, SOCK_STREAM)  # create socket object
sockobj.connect((serverHost, serverPort))   # connect to server using port
for line in message:
    sockobj.send(line)  # send the line of message to server
    data = sockobj.recv(1024)   # receive data from server with buffer 1k
    print('Clint received:', data)  # bytes type string will be shown like "x", repr(x)

sockobj.close()