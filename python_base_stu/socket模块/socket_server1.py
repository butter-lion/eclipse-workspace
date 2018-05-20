'''
Created on 2018年5月15日

@author: zhang
'''

import socket,os,hashlib

server = socket.socket()
server.bind(('localhost',3456))
server.listen()
#等待接入

while True:
    print('等待新客户接入')
    #客户接入
    conn,addr = server.accept() 
    print(conn,addr)
    print('客户已接入')
    while True:
        #接受客户端请求
        data = conn.recv(1024)
        #如果断开 跳出循环
        if not data: 
            print('客户已断开')
            break
        #解析客户需求
        cmd,filename = data.decode().split()
        #如果cmd == ‘get’ 且 文件存在开始传输
        if cmd.startswith('get') and os.path.isfile(filename):
            #获取并传输文件大小
            size = str(os.path.getsize(filename))
            conn.send(size.encode(encoding='utf_8', errors='strict'))
            #接受准备完毕信号
            sign = conn.recv(1024)
            print('开始传输数据')
            #打开文件并循环传输
            m = hashlib.md5()
            with open(filename,'rb') as f:
                for line in f.readlines():
                    m.update(line)
                    conn.send(line)
            print('send final!')
            conn.send(m.hexdigest().encode('utf-8'))        
        else:
            conn.send(b'Not Found File')        
        
server.close()   