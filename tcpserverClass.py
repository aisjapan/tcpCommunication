import socket
import threading

class tcpserver(socket.socket, threading.Thread):
    def __init__(self):
        self._host = ""
        self._port = None
        self._serversock = None
        self._maxClients = 0
        self._recievedMsg = []
        self._clientSock = []
        self._serverThread = None

    def setServer(self,host,port,maxClients):
        self._host = host
        self._port = port
        self._maxClients = maxClients

    def __server(self):
        for i in range(self._maxClients):
            self._clientSock.append(self._serversock.accept())
            print(self._clientSock[i][1])

    def sendAll(self,msg):
        for e in self._clientSock:
            e[0].sendall(msg.encode('utf-8'))

    def __recieve(self):
        while True:
            for e in self._clientSock:
                rcvmsg = e[0].recv(4096)
                self._recievedMsg.append(rcvmsg.decode('utf-8'))

    def getMsg(self):
        if len(self._recievedMsg) != 0:
            msg = self._recievedMsg[0]
            self._recievedMsg.pop(0)
            return True,msg
        else:
            return False, ''

    def startServer(self):
        self._serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._serversock.bind((self._host,self._port)) #IPとPORTを指定してバインドします
        self._serversock.listen(10) #接続の待ち受けをします（キューの最大数を指定）
        self._serverThread = threading.Thread(target=self._server, name="server",args=())
        self._recieveThread = threading.Thread(target=self._recieve, name= "recieve",args=())
        self._serverThread.setDaemon(True)
        self._recieveThread.setDaemon(True)
        self._serverThread.start()
        self._recieveThread.start()
