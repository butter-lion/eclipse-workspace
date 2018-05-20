'''
Created on 2018年5月14日

@author: zhang
'''

# 客户端
import socket

client = socket.socket()
client.connect(('localhost', 9000))
while True:
    message = input('>>:').strip()
    if message == '':
        print('please enter :')
        continue
    client.send(message.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode())

client.close()
