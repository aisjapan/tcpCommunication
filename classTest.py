import tcpserverClass
import socket
import threading
import time
import aisprotocol

server = tcpserverClass.tcpserver()

robotinfo = []

server.setServer('192.168.3.127',445,10)

server.startServer()

count = 0

while True:
    status, msg = server.getMsg()

    if status and msg != '':
        print(msg)
        if msg == 'READY':
            count = count + 1
        if count == 1:
            server.sendAll("START")
