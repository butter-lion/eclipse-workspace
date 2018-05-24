'''
Created on 2018年5月23日

@author: zhang
'''
import socket
import sys
import os
import json

def ProcessBar(part, total):  ####进度条模块，只能在Linux下使用，并且窗口宽度要足够宽，否则会变成多行显示
    if total != 0:
        i = round(part * 100 / total)
        sys.stdout.write(
            '[' + '>' * i + '-' * (100 - i) + ']' + str(i) + '%' + ' ' * 3 + str(part) + '/' + str(total) + '\r')
        sys.stdout.flush()

class FtpClient(object):
    def __init__(self,conn):
        self.conn = conn

    def get(self,filename):
        msg_send = {"motion": "get",
                    "filename": filename,
                    "filesize":0,
                    "md5":''}
        self.conn.send(json.dumps(msg_send).encode("utf-8"))
        msg_recv = self.conn.recv(1024)
        msg=json.loads(msg_recv.decode("utf-8"))
        filesize = msg["filesize"]
        filemd5 = msg["md5"]
        recv_size = 0
        f = open(filename,"wb")
        while filesize > recv_size:
            if filesize - recv_size > 1024:
                n = 1024
            else:
                n = filesize - recv_size
            r_data = self.conn.recv(n)
            f.write(r_data)
            recv_size += len(r_data)
            ProcessBar(recv_size, filesize)
        f.close()
        recv_filemd5 = 123456
        print("filename:", filename, "filesize", filesize, "recv_size:", recv_size,"recv_filemd5:",recv_filemd5,"original_filemd5:",filemd5)

    def put(self,filename):
        filesize = os.path.getsize(filename)
        filemd5 = 123456
        msg = {"motion":"put",
               "filename":filename,
               "filesize":filesize,
               "md5":filemd5}
        self.conn.send(json.dumps(msg).encode("utf-8"))
        self.conn.recv(1024)    ####防止粘包信号
        sendsize = 0
        f = open(filename, "rb")
        for line in f:
            self.conn.send(line)
            sendsize += len(line)
            ProcessBar(sendsize, filesize)
        f.close()
        print(filename," transfer complete！")
    def interactive(self):
        while True:
            cmd = input(">>>:").strip()
            if len(cmd) == 0:
                continue
            elif cmd == "exit":
                exit()
            else:
                motion = cmd.split()[0]
                if hasattr(self,motion):
                    filename = cmd.split()[1]
                    func = getattr(self,motion)
                    func(filename)
                else:
                    self.conn.send(json.dumps(cmd).encode("utf-8"))
                    msg = self.conn.recv(1024)
                    print("Server feedback,command error:",json.loads(msg.decode("utf-8")))

if __name__ == "__main__":
    sock = socket.socket()
    sock.connect(('127.0.0.1',9999))
    c = FtpClient(sock)
    c.interactive()