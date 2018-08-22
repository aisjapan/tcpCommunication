import socket
import threading

class tcpClient(socket.socket):
    """docstring for tcpClient."""
    def __init__(self):
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__recievedMsg = []

    def setHost(self,host,port):
        self.__host = host
        self.__port = port

    def connect(self):
        self.__client.connect((self.__host,self.__port))

    def send(self,msg):
        self.__client.send(msg)

    def recieve(self):
        return self.__client.recv(4096)

    def __recieve(self):
        while True:
            rcvmsg = self.__client.recv(4096)
            self.__recievedMsg.append(rcvmsg.decode('utf-8'))

    def getMsg(self):
        if len(self.__recievedMsg) != 0:
            msg = self.__recievedMsg[0]
            self.__recievedMsg.pop(0)
            return True,msg
        else:
            return False, ''


    def startRecieve(self):
        self.__recieveThread = threading.Thread(target=self.__recieve, name="recieve",args=())
        self.__recieveThread.setDaemon(True)
        self.__recieveThread.start()
