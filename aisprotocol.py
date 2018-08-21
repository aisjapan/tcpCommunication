# IP:COLOR:DATATYPE:DATA:DATATYPE:DATA

def isOnTable(search_ip,robotinfo):
    for i, e in enumerate(robotinfo):
        if e.ip == search_ip:
            return True, i
    return False, None



class robotInfo(object):
    """docstring for robotInfo."""
    def __init__(self,ip = "8.8.8.8",color = "BLACK"):
        self.posX = 0.0
        self.posY = 0.0
        self.state = "WAIT_CONN"
        self.color = color
        self.ip = ip

    def __str__(self):
        return "IP:{0:10} | COLOR:{1:10} | STATE:{2:10}".format(self.ip,
                                                                self.color,
                                                                self.state)

class aisProtocol():
    """docstring for aisProtocol."""
    def __init__(self,ip,color):
        self.__ip = ip
        self.__color = color
        self.__sendingData = []

    def addData(self,datatype,data):
        self.__sendingData.extend([datatype,data])

    def buildData(self):
        builtData = self.__ip + ":" +  self.__color
        for e in self.__sendingData:
            builtData = builtData + ":" + e
        return builtData

    def clearData(self):
        self.__sendingData = []

    def decodeData(self,data):
        decode = data.split(":")
        ip = decode[0]
        color = decode[1]
        decode.pop(0)
        decode.pop(0)
        i = 0
        datalist = []
        while i*2+1 < len(decode):
            #一次元のデータを二次元に
            datalist.append((decode[i*2],decode[i*2 + 1]))
            i = i + 1

        return ip, color, datalist

    def __str__(self):
        return self.buildData()
