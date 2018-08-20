import tcpserverClass
import tcpclientClass
import socket
import threading
import time

server = tcpserverClass.tcpserver()
c = tcpclientClass.tcpClient()

server.setServer('192.168.43.22',445,10)
c.setHost('192.168.4.1',8080)

server.startServer()
c.connect()

while True:
    status, msg = server.getMsg()
    if status:
        print(msg)
        msg = "recieved" + msg
        c.send(msg.encode('utf-8'))
