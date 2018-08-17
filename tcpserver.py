# -*- coding:utf-8 -*-
import socket
import sys
import time
import threading

ROBOMAXNUM = 10
CLIENT_ACTIVE = True
CLIENT_INACTIVE = False
host = "192.168.3.127" #Server Host name
port = 445 #port
TIME_HEADER = 'CN:'
startingTime = time.time()
clientSock = []
rcvmsg = []
i = 0

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind((host,port)) #IPとPORTを指定してバインドします
serversock.listen(10) #接続の待ち受けをします（キューの最大数を指定）

def server():
    for i in range(ROBOMAXNUM):
        clientSock.append(serversock.accept())
        print("connected" + str(clientSock[i][1]))

def recieve():
    while True:
        for e in clientSock:
            try:
                rcvmsg = e[0].recv(1024)
                print("recieved" + rcvmsg.decode('utf-8'))
            except:
                print("recieving Error")

def send():
    while True:
        for e in clientSock:
            s_msg = TIME_HEADER + str(time.time()-startingTime)
            e[0].sendall(s_msg.encode('utf-8'))
        time.sleep(1)

th1 = threading.Thread(target=server,name="server",args=())
th2 = threading.Thread(target=recieve,name="recieve",args=())
th3 = threading.Thread(target=send,name="send",args=())

th1.setDaemon(True)
th2.setDaemon(True)
th3.setDaemon(True)
th1.start()
time.sleep(0.1)
th2.start()
th3.start()
while True:
    print("running")
    time.sleep(1)
clientsock.close()
