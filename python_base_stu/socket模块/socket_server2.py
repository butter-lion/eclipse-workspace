'''
Created on 2018年5月15日

@author: zhang
'''

import socket,os

server = socket.socket()
server.bind(('localhost',3456))
server.listen()
#等待接入

while True:
    print('等待客户接入')
    #客户接入
    conn,addr = server.accept() 
    print(conn,addr)
    print('客户已接入')
    while True:
        #接受客户端请求
        data = conn.recv(1024)
        #处理请求
        if not data: break
        res = os.popen(data.decode()).read()
        #传送长度
        print('123')
        conn.send(str(len(res.encode('utf-8'))).encode())
        #去除粘连
        res_msg = conn.recv(1024)
        print('开始传输数据')
        #传输数据
        conn.send(res.encode('utf-8'))
        print('asas')
        if not data:
            break
        
server.close()   