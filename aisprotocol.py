# IP:COLOR:DATATYPE:DATA:DATATYPE:DATA

def isOnTable(search_ip,robotinfo):
    for i, e in enumerate(robotinfo):
        if e.ip == search_ip:
            return True, i
    return False, None

def decodeData(data):
    decode = data.split(":")
    if len(decode) < 2:
        print("ERROR:wrong protocol")
        print(decode)
        return '', '', ''
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

class robotInfo():
    """docstring for robotInfo."""
    def __init__(self,ip = "8.8.8.8",color = "BLACK"):
        self.angle = 0.0
        self.distance = 0.0
        self.state = "WAIT_CONN"
        self.color = color
        self.ip = ip
        self.rawMsg = ''
        self.msg = ' '

    def buildData(self):
        builtData = self.ip + ":" + \
                    self.color + ":" + \
                    "STATE:" + self.state + ":" + \
                    "ANGLE:" + str(self.angle) + ":" + \
                    "DIST:" + str(self.distance) + ":" + \
                    "MSG:" + self.msg

        self.rawMsg = builtData
        return builtData

    def rawMsg2obj(self,msg):
        ip, color, datalist = decodeData(msg)
        if not ip == self.ip and color == self.color:
            return False

        for dataType, data in datalist:
            if dataType == "ANGLE":
                self.angle = float(data)
            elif dataType == "DIST":
                self.distance = float(data)
            elif dataType == "STATE":
                self.state = data
            elif dataType == "MSG":
                self.msg = data
            else:
                print("protocolError" + dataType)
                return False
        return True

    def __str__(self):
        return "IP:{0:17} | COLOR:{1:10} | STATE:{2:10} | msg:{3:10}".format(self.ip,
                                                                             self.color,
                                                                             self.state,
                                                                             self.msg)
