'''
Created on 2018年5月14日

@author: zhang
'''

#客户端
import socket

client = socket.socket()
client.connect(('localhost',6969))
while True:
    message = input('>>:').strip()
    client.send(message.encode('utf-8'))
    data = client.recv(1024)
    with open('buhao.jpg','wb') as f:
        f.write(data)

client.close()
