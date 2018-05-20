'''
Created on 2018年5月14日

@author: zhang
'''
#服务端

import socket,os

server = socket.socket()
server.bind(('localhost',6969))#绑定要监听的端口
server.listen()#监听
while True:
    print('我要等电话了')
    conn,addr =server.accept()#等电话打进来
    #conn就是客户端连过来而在服务器端为其生成的一个连接实例
    print(conn,addr)
     
    print('电话来了')
    while True:
        data = conn.recv(1024)
        print('recv:',data)
        with open('nihao.jpg','rb') as f:
            conn.sendall(f.read())
        if not data:
            break
server.close()