'''
Created on 2018年5月17日

@author: zhang
'''

import socket
import os
import json
import getpass
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
class FtpClient(object):

    def connect(self,ip,port):
        self.client.connect((ip,port))

    def __init__(self):
        self.client = socket.socket()

    def cmd_help(self,*args):
        msg = '''
        ls
        pwd
        cd../..
        get filename
        put filename
        '''
        print(msg)

    def cmd_ls(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) == 1:
            msg_dic = {
                'action': 'ls',
                'overridden': True
                }
            self.client.send(json.dumps(msg_dic).encode('utf-8'))
            msg = (self.client.recv(1024)).decode()
            m = json.loads(msg)
            print(m)

    def enter_sys(self):
        username = input("username:")
        password = input("password:")
        msg_dic = {
                'username': username,
                'password': password
                }
        self.client.send(json.dumps(msg_dic).encode('utf-8'))


    def cmd_register(self):
        print('start register, please enter your info:')
        username = input('enter your username:')
        password = ''
        while True:
            p1 = input('enter your password:')
            p2 = input('enter your password again:')
            if p1 == p2:
                password = p1
                break
            else:
                print('Two passwords are different:')
        msg_dic = {
            'action': 'register',
            'username': username,
            'password': password,
            'overridden': True
        }
        self.client.send(json.dumps(msg_dic).encode('utf-8'))
        # 防止粘包，等服务器确认
        print(json.dumps(msg_dic).encode('utf-8'))
        server_response = (self.client.recv(1024)).decode()
        if server_response == '200 OK':
            print('用户创建成功')
        else:
            print('用户创建失败')
            return ftp.cmd_register()

    def interactive(self):
        #进行用户登陆验证，成功才进行下一步操作
        while True:
            print('请输入用户账户和密码')
            self.enter_sys()
            msg = self.client.recv(1024)
            if msg.decode() == '200 OK':
                break
            else:
                print('用户名不存在或密码错误')
        while True:
            cmd = input('>>:').strip()
            if len(cmd) == 0: continue
            cmd_str = cmd.split()[0]
            print (cmd_str)
            if hasattr(self,'cmd_%s' % cmd_str):
                func = getattr(self,'cmd_%s' % cmd_str)
                func(cmd)
            else:
                self.cmd_help()

    def cmd_put(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.path.getsize(filename)
                msg_dic = {
                    'action': 'put',
                    'filename': filename,
                    'size': filesize,
                    'overridden': True
                }
                self.client.send(json.dumps(msg_dic).encode('utf-8'))
                #防止粘包，等服务器确认
                print(json.dumps(msg_dic).encode('utf-8'))
                server_response =(self.client.recv(1024)).decode()
                if server_response == '200 OK':
                    with open(filename, 'rb') as f:
                        for line in f.readlines():
                            self.client.send(line)
                        else:
                            print('file upload success ...')
            else:
                print('文件不存在')

    def cmd_get(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            msg_dic = {
                'action': 'get',
                'filename': filename,
                'overridden': True
                }
            self.client.send(json.dumps(msg_dic).encode('utf-8'))
            # 防止粘包，等服务器确认
            print(json.dumps(msg_dic).encode('utf-8'))
            filesize = int(self.client.recv(1024).decode())
            if filesize == 0:
                print('服务器没有这个文件')
            else:
                print(filesize)
                self.client.send(b'200 ok')
                if os.path.isfile(filename):
                    f = open('new' + filename, 'wb')
                    print('file is exist,creat a new file', 'new' + filename)

                else:
                    f = open(filename, 'wb')
                received_size = 0
                while received_size < filesize:
                    if filesize - received_size > 1024:
                        recover_size = 1024
                    else:
                        recover_size = filesize - received_size
                    res_data = self.client.recv(recover_size)
                    received_size += len(res_data)
                    f.write(res_data)
                    print('接收到', received_size, '字节')
                else:
                    print('file [%s] has loaded...' % filename)
                f.close()
    def run(self):
        while True:
            print('''
            1、注册
            2、登陆''')
            a = input('>>:')
            self.client.send(a.encode('utf-8'))
            if a == '1':
                ftp.cmd_register()
                self.client.send(b'register')
            if a == '2':
                ftp.interactive()

ftp = FtpClient()
ftp.connect('localhost',9000)
ftp.run()