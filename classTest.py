import tcpserverClass
import socket
import threading
import time

server = tcpserverClass.tcpserver()

server.setServer('10.0.0.23',445,10)

server.startServer()

while True:
    status, msg = server.getMsg()
    if status:
        print(msg)
