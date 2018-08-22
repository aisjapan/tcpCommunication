# -*- coding:utf-8 -*-
import socket
import time
import aisprotocol
import tcpclientClass

host = "10.0.0.23" #お使いのサーバーのホスト名を入れます
port = 445 #適当なPORTを指定してあげます
startingTime = time.time()

def getCurrentTime():
    return time.time() - startingTime

client = tcpclientClass.tcpClient() #オブジェクトの作成をします

client.setHost(host, port) #これでサーバーに接続します
client.connect()

client.startRecieve()

robotinfo = []
robotinfo.append(aisprotocol.robotInfo())

while True:
    time.sleep(1)
    client.send(robotinfo[0].buildData().encode('utf-8')) #適当なデータを送信します（届く側にわかるように）
    status, msg = client.getMsg()
    print(msg)
    print("time" + str(getCurrentTime()))
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
