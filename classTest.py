import tcpserverClass
import socket
import threading
import time
import aisprotocol

server = tcpserverClass.tcpserver()

formatter = aisprotocol.aisProtocol()


server.setServer('192.168.3.127',445,10)

server.startServer()

while True:
    status, msg = server.getMsg()

    if status:
        server.sendAll(msg)
        formatter.decodeData(msg.decode('utf-8'))
