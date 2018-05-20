'''
Created on 2018年5月15日

@author: zhang
'''
import socket

client = socket.socket()
#进行连接
client.connect(('localhost',3456))
while True:
    data = input('>>:').strip()
    client.send(data.encode(encoding='utf_8'))
    res_size = int(client.recv(1024))
    print(res_size)
    size = 0
    res  = b''
    client.send(b'Please send data!')
    while res_size != size:
        res_data = client.recv(124)
        size += len(res_data)
        res += res_data
    print('接收到',size,'字节')
    print(res.decode())
client.close()    