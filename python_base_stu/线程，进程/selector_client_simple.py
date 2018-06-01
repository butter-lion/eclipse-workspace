'''
Created on 2018年5月24日

@author: zhang
'''
import json
import os
import socket


class FTPclient(object):
    def __init__(self,conn):
        self.conn = conn

    def get(self,filename):
        msg_send = {
            'action':'get',
            'filename':filename
        }
        self.conn.send(json.dumps(msg_send).encode('utf-8'))
        msg_recv = json.loads(self.conn.recv(1024).decode())
        print(msg_recv)
        filesize = msg_recv['filesize']
        recv_size = 0
        f = open(filename, "wb")
        while filesize > recv_size:
            if filesize - recv_size > 1024:
                n = 1024
            else:
                n = filesize - recv_size
            r_data = self.conn.recv(n)
            f.write(r_data)
            recv_size += len(r_data)
            print(recv_size)
        f.close()
        print("filename:", filename, "filesize", filesize, "recv_size:", recv_size, )

    def put(self,filename):
        filesize = os.path.getsize(filename)
        msg_send = {
            'action':'put',
            'filename':filename,
            'filesize':filesize
        }
        self.conn.send(json.dumps(msg_send).encode('utf-8'))
        msg_recv = self.conn.recv(1024).decode()
        print(msg_recv)
        f = open(filename, "rb")
        for line in f:
            self.conn.send(line)
        f.close()
        print("filename:", filename, "filesize", filesize, "send ok:" )

    def dir(self):
        msg_send = {
            'action':'dir'
        }
        self.conn.send(json.dumps(msg_send).encode('utf-8'))
        msg_recv = self.conn.recv(1024).decode()
        print(msg_recv)

    def interactive(self):
        while True:
            cmd = input(">>>:").strip()
            if len(cmd) == 0:
                continue
            elif cmd == "exit":
                exit()
            elif cmd == 'ls':
                self.dir()
            else:
                action = cmd.split()[0]
                if hasattr(self,action):
                    filename = cmd.split()[1]
                    func = getattr(self,action)
                    func(filename)
                else:
                    self.conn.send(json.dumps(cmd).encode("utf-8"))
                    msg = self.conn.recv(1024)
                    print("Server feedback,command error:",json.loads(msg.decode("utf-8")))

if __name__ == '__main__':
    sock = socket.socket()
    sock.connect(('localhost',8899))
    c = FTPclient(sock)
    c.interactive()
