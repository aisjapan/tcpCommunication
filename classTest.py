import tcpserverClass
import socket
import threading
import time
import aisprotocol

server = tcpserverClass.tcpserver()

robotinfo = []

robotinfo.append(aisprotocol.robotInfo())
robotinfo[0].state = "WAIT_CONN"
robotinfo[0].color = "BLUE"
robotinfo[0].ip = "192.168.3.50"

server.setServer('10.0.0.23',445,10)

server.startServer()



while True:
    status, msg = server.getMsg()

    if status:
        sender_ip,sender_color,datalist = aisprotocol.decodeData(msg)

        onTable,robotIndex = aisprotocol.isOnTable(sender_ip,robotinfo)
        if not onTable:
            robotinfo.append(aisprotocol.robotInfo(sender_ip,sender_color))
            robotIndex = len(robotinfo)-1

        if not robotinfo[robotIndex].rawMsg2obj(msg):
            print("ERROR in processing data")


        for e in robotinfo:
            print(e)
        for e in robotinfo:
            e.buildData()
            print(e.rawMsg)
            server.sendAll(e.rawMsg)
