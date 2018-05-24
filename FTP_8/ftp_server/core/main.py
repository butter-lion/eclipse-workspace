'''
Created on 2018年5月17日

@author: zhang
'''

import socketserver
import json
import os,sys
import selectors

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from core import data

sel = selectors.DefaultSelector()

def accept(sock,mask):
    conn,addr = sock.accept()
    print('accept:',conn,'from',addr)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,MyTCPHandler.handle)

class MyTCPHandler(socketserver.BaseRequestHandler):

    def accept(self, mask):
        conn, addr = self.request.accept()
        print('accept:', conn, 'from', addr)
        conn.setblocking(False)
        sel.register(conn, selectors.EVENT_READ, MyTCPHandler.handle)

    def register(self,*args):
        cmd_dic = args[0]
        username = cmd_dic['username']
        password = cmd_dic['password']
        infos = data.loads()
        if username in infos:
            self.request.send(b'404 NOT')
        else:
            infos[username] = {
                'username': username,
                'password': password,
                'datapath': 'C:/Users/zhang/Desktop/eclipse-workspace/FTP_8/ftp_server/data/%s' % username,
                'datasize': 0,
                'maxsize': 1024000
            }
            data.dump(infos)
            os.chdir('C:/Users/zhang/Desktop/eclipse-workspace/FTP_8/ftp_server/data')
            os.makedirs(username)
            self.request.send(b'200 OK')
            print("new user creat success")


    def enter_sys(self,*args):
        cmd_dic = args[0]
        username = cmd_dic['username']
        password = cmd_dic['password']
        infos = data.loads()
        if username in infos and infos[username]['password'] == password:
            info = infos[username]
            os.chdir(info['datapath'])
            self.request.send(b'200 OK')
            return username
        else:
            self.request.send(b'404 NOT')
            return False
        
    def ls (self,*args):
        file = os.getcwd()
        print(file)
        msg = os.listdir(file)
        m = json.dumps(msg)
        print(m)
        self.request.send(m.encode('utf-8'))
        
    
    def put(self,*args):
        # 接收客户端文件
        cmd_dic = args[0]
        filename = cmd_dic['filename']
        filesize = cmd_dic['size']
        if os.path.isfile(filename):
            f = open('new'+filename,'wb')
            print('file is exist,creat a new file', 'new'+filename)

        else:
            f = open(filename,'wb')

        self.request.send(b'200 OK')
        received_size = 0
        while received_size < filesize:
            if filesize - received_size >1024:
                recover_size = 1024
            else:
                recover_size = filesize - received_size
            res_data = self.request.recv(recover_size)
            received_size += len(res_data)
            f.write(res_data)
            print('start unloaded [%s]' % filename)
            print('接收到',received_size,'字节')
        else:
            print('file [%s] has uploaded...' % filename)
        f.close()

    def get(self,*args):
        # 接收客户端文件
        cmd_dic = args[0]
        filename = cmd_dic['filename']
        if os.path.isfile(filename):
            filesize = str(os.path.getsize(filename))
            self.request.send(filesize.encode('utf-8'))
            server_response = self.request.recv(1024)
            print(server_response)
            with open(filename, 'rb') as f:
                print('file [%s] start send ...' % filename)
                for line in f.readlines():
                    self.request.send(line)
                else:
                    print('file send success ...')
        else:
            filesize = b'0'
            self.request.send(filesize)

    def handle(self):
        re = (self.request.recv(1024)).decode()
        while True:
            if re == '1':
                break
            #获取登录信息
            self.data = self.request.recv(1024).strip()
            #打印服务器端地址
            print('{} wrote:'.format(self.client_address[0]))
            cmd_dic = json.loads(self.data.decode())
            #验证登陆信息
            username = self.enter_sys(cmd_dic)
            #成功进行下一步，不成功重新登陆
            if username:
                print('登陆成功')
                break
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic['action']
                if action == 'put':
                    infos = data.loads()
                    infos[username]['datasize'] +=cmd_dic['size']
                    if infos[username]['datasize'] > infos[username]['maxsize']:
                        print('文件太大了，不能上传')
                        self.request.send(b'404 NOT')
                        continue
                    else:
                        data.dump(infos)
                if hasattr(self,action):
                    func = getattr(self,action)
                    func(cmd_dic)

            except ConnectionResetError as e:
                print('出错了',e)
                break


if __name__ == '__main__':
    HOST,PORT = 'localhost' , 9000
    # creat the server,blinding to localhost on port
    server = socketserver.TCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()
