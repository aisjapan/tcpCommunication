# -*- coding:utf-8 -*-
import socket
import time
import threading

host = "10.0.0.23"
port = 445
TIME_HEADER = "JP:"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))
startingTime = time.time()

def recieve():
    try:
        response = client.recv(4096)


def send():
    try:
        client.send(TIME_HEADER+ str(time.time()))

th1 = threading.Thread(target=recieve,name="recieve",args=())
th2 = threading.Thread(target=send,name="send",args=())
th1.setDaemon(True)
th2.setDaemon(True)
th1.start()
th2.start()
