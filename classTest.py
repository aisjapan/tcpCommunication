import tcpserverClass
import socket
import threading
import time
import aisprotocol

server = tcpserverClass.tcpserver()

formatter = aisprotocol.aisProtocol("192.168.3.50","BLUE")

robotinfo = []

robotinfo.append(aisprotocol.robotInfo())
robotinfo[0].state = "WAIT_CONN"
robotinfo[0].color = "BLUE"
robotinfo[0].ip = "192.168.3.50"

server.setServer('10.0.0.23',445,10)

server.startServer()



while True:
    status, msg = server.getMsg()

    if status or True:
        server.sendAll(msg)
        msg = "192.168.3.51:YELLOW:POSX:1.000:POSY:3.21:STATE:RDY"
        sender_ip,sender_color,datalist = formatter.decodeData(msg)

        onTable,robotIndex = aisprotocol.isOnTable(sender_ip,robotinfo)
        if not onTable:
            robotinfo.append(aisprotocol.robotInfo(sender_ip,sender_color))
            robotIndex = len(robotinfo)-1

        for e in datalist:
            if e[0] == "POSX":
                robotinfo[robotIndex].posX = float(e[1])
            elif e[0] == "POSY":
                robotinfo[robotIndex].posY = float(e[1])
            elif e[0] == "STATE":
                robotinfo[robotIndex].state = e[1]
            else:
                print("protocolError")

        for e in robotinfo:
            print(e)

        time.sleep(1)
