"""
Opens socket TCP/IP on the server's side
"""
from socket import *
myHost = ''
myPort = 50007
sockobj = socket(AF_INET, SOCK_STREAM)   #create socket object
sockobj.bind((myHost, myPort))  # bind with port
sockobj.listen(5)   # waiting up to 5 requests

while True:
    connection, address = sockobj.accept()  # wait for client's request while working
    print('Server connected by', address)

    while True:
        data = connection.recv(1024)    # read next line from socket
        if not data: break
        connection.send(b'Echo=>' + data)   # send answer to client while data exists
    connection.close()
