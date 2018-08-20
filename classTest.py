import tcpserverClass
import socket
import threading
import time

server = tcpserverClass.tcpserver()

server.setServer('192.168.3.127',445,10)

server.startServer()

while True:
    status, msg = server.getMsg()
    if status:
        print(msg)
        server.sendAll("HELLO FROM SERVER")
        
