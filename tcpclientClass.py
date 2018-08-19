import socket

class tcpClient(socket.socket):
    """docstring for tcpClient."""
    def __init__(self):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def setHost(self,host,port):
        self._host = host
        self._port = port

    def connect(self):
        self._client.connect((self._host,self._port))

    def send(self,msg):
        self._client.send(msg)

    def recieve(self):
        return self._client.recv(4096)
