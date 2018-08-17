# -*- coding:utf-8 -*-
import socket
import time

host = "10.0.0.23" #お使いのサーバーのホスト名を入れます
port = 445 #適当なPORTを指定してあげます
TIME_HEADER = "JP:"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします

client.connect((host, port)) #これでサーバーに接続します
startingTime = time.time()

while True:
    currentTime = time.time()-startingTime
    client.send(TIME_HEADER + str(currentTime)) #適当なデータを送信します（届く側にわかるように）
    time.sleep(1)
