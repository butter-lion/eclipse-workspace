'''
Created on 2018年5月18日

@author: zhang
'''

import getpass
import os,sys
from ftp_server.core import data

# 注册
def register():
    print('start register, please enter your info:')
    username = input('enter your username:')
    password = ''
    while True:
        p1 = getpass.getpass('enter your password:')
        p2 = getpass.getpass('enter your password again:')
        if p1 == p2:
            password = p1
            break
        else:
            print('Two passwords are different:')
    infos = data.loads()
    infos[username] = {
        'username':username,
        'password':password,
        'datapath': 'C:/Users/zhang/Desktop/eclipse-workspace/FTP_8/ftp_server/data/%s' % username,
        'datasize': 0,
        'maxsize': 1024000
    }
    data.dump(infos)
    os.chdir('C:/Users/zhang/Desktop/eclipse-workspace/FTP_8/ftp_server/data')
    os.makedirs(username)
    print("new user creat success")


# 登陆
def login():
    username = input('enter your username:')
    password = getpass.getpass('enter your password:')
    infos = data.loads()
    if username in infos and infos[username]['password'] == password:
        return data.load(username)
    else:
        print('username is not exist or password wrong!')
        return login()

if __name__ == '__main__':
    
    register()