import socket
import threading
import time

class tcpserver(socket.socket, threading.Thread):
    def __init__(self):
        self.__host = ""
        self.__port = None
        self.__serversock = None
        self.__maxClients = 0
        self.__recievedMsg = []
        self.__clientSock = []
        self.__recieveThread = []
        self.__serverThread = None

    def setServer(self,host,port,maxClients):
        self.__host = host
        self.__port = port
        self.__maxClients = maxClients

    def sendAll(self,msg):
        for client_socket, _ in self.__clientSock:
            client_socket.sendall(msg.encode('utf-8'))

    def __recieve(self,socketObject):
        while True:
            rcvmsg = socketObject.recv(4096)
            self.__recievedMsg.append(rcvmsg.decode('utf-8'))
            time.sleep(0.01)

    def __server(self):
        for i in range(self.__maxClients):
            self.__clientSock.append(self.__serversock.accept())
            print(self.__clientSock[i][1])
            self.__recieveThread.append(threading.Thread(target=self.__recieve, name="recieve"+ str(i),args=(self.__clientSock[i][0],)))
            self.__recieveThread[i].setDaemon(True)
            self.__recieveThread[i].start()

    def getMsg(self):
        if len(self.__recievedMsg) != 0:
            msg = self.__recievedMsg[0]
            self.__recievedMsg.pop(0)
            return True,msg
        else:
            return False, ''

    def startServer(self):
        self.__serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__serversock.bind((self.__host,self.__port)) #IPとPORTを指定してバインドします
        self.__serversock.listen(10) #接続の待ち受けをします（キューの最大数を指定）
        self.__serverThread = threading.Thread(target=self.__server, name="server",args=())
        self.__serverThread.setDaemon(True)
        self.__serverThread.start()
