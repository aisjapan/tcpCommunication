# IP:COLOR:DATATYPE:DATA:DATATYPE:DATA



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

    def decodeData(data):
        decode = data.split(":")
        ip = decode[0]
        color = decode[1]
        decode.pop(0)
        decode.pop(1)
        i = 0
        while i < len(decode):
            #一次元のデータを二次元に
            datalist[i][0] = decode[i*2]
            datalist[i][1] = decode[i*2 + 1]
            i = i + 1

        return ip, color, datalist

    def __str__(self):
        return self.buildData()
