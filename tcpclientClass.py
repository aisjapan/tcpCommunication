import socket

class tcpClient(socket.socket):
    """docstring for tcpClient."""
    def __init__(self):
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def setHost(self,host,port):
        self.__host = host
        self.__port = port

    def connect(self):
        self.__client.connect((self.__host,self.__port))

    def send(self,msg):
        self.__client.send(msg)

    def recieve(self):
        return self.__client.recv(4096)
