import tcpserverClass
import socket
import threading
import time
import aisprotocol
import serial


#--------------追記------------------
#Json
f = open('RaspberryPiMessage_A.json', 'r')
send_message_dict = json.load(f)

#Serial
port = "/dev/ttyS0"
serialFromArduino = serial.Serial(port, 115200)
serialFromArduino.flushInput()


#Serial Communication
def SendJson2Due():
  # MessageTypeはデフォルトで0　そして1で動くように高野にArduino側のプログラムを変更してもらう
  send_message_dict["MessageType"] = 1

  send_str = json.dumps(send_message_dict)
  send_str = send_str + '\n'
  serialFromArduino.write(bytes(send_str.encode("utf-8")))
  print(send_str)
  t=threading.Timer(1,SendJson2Due)
  t.start()

#------------------------------------


server = tcpserverClass.tcpserver()

robotinfo = []

server.setServer('192.168.3.127',445,10)

server.startServer()

count = 0

while True:
    status, msg = server.getMsg()

    if status and msg != '':
        print(msg)
        if msg == 'READY':
            count = count + 1
        if count == 3:
            server.sendAll("START")
            
            t=threading.Thread(target=SendJson2Due)
            t.start()

serialFromArduino.close()