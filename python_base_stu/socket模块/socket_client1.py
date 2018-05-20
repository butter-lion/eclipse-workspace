'''
Created on 2018年5月15日

@author: zhang
'''
import socket ,hashlib

client = socket.socket()
#进行连接
client.connect(('localhost',3456))
while True:
    data = input('>>:').strip()
    cmd,filename = data.split()
    client.send(data.encode(encoding='utf_8'))
    res_size = client.recv(1024).decode()
    if res_size == 'Not Found File':
        print('文件不存在')
        continue
    else:
        res_size = int(res_size)
        print(res_size)
        size = 0
        m = hashlib.md5()
        client.send(b'Please send data!')
        with open('new'+filename,'wb') as f:
        
            while res_size > size:
                if res_size - size >1024:
                    recover_size = 1024
                else:
                    recover_size = res_size-size
                res_data = client.recv(recover_size)
                size += len(res_data)
                m.update(res_data)
                f.write(res_data)
        print('接收到',size,'字节')
        send_md5 = client.recv(1024).decode()
        new_md5 = m.hexdigest()
        print(send_md5)
        print(new_md5)
client.close()    