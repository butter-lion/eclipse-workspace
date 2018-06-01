'''
Created on 2018年5月24日

@author: zhang
'''
import json
import os
import selectors
import socket


class FTPserver(object):
    def __init__(self,sock):
        self.sel = selectors.DefaultSelector()
        self.sock = sock
        self.down_dict = {}
        self.up_dict ={}
        '''down_dict={conn:{
                            'action':'get',
                            'filename':filename,
                            'rfb':fb，               #打开的文件句柄
                            'send_size':0
                            'filesize':os.path.getsize(filename)
        }'''

    def start(self):
        self.sock.listen(1000)
        self.sock.setblocking(False)
        self.sel.register(sock, selectors.EVENT_READ, self.accept)
        while True:
            events = self.sel.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj)

    def accept(self,sock):
        conn, addr = sock.accept()
        print('accepted', conn, 'from', addr)
        conn.setblocking(False)
        self.sel.register(conn, selectors.EVENT_READ, self.read)

    def read(self,conn):
        try:
            data = conn.recv(1024)
            print("read:", conn, "data:", data)
            if data:
                try:
                    msg = json.loads(data.decode("utf-8"))
                    print("msg:",msg,"from conn:",conn)
                    action = msg["action"]
                    if "get" == action:
                        filename = msg["filename"]
                        msg['filesize'] = os.path.getsize(filename)
                        conn.send((json.dumps(msg)).encode("utf-8"))
                        msg["send_size"] = 0
                        fd = open(filename, "rb")
                        msg["rfd"] = fd
                        print(msg)
                        self.down_dict[conn] = msg
                        self.sel.modify(conn, selectors.EVENT_WRITE, self.download)

                    elif "put" == action:
                        filename = msg["filename"]
                        msg["get_size"] = 0
                        fd = open(filename, "wb")
                        msg["wfd"] = fd
                        self.up_dict[conn] = msg
                        conn.send(b'ready to recieve')
                        self.sel.modify(conn, selectors.EVENT_READ, self.updata)
                    elif action == 'dir':
                        self.sel.modify(conn, selectors.EVENT_WRITE, self.dir)
                    else:
                        print('func matching miss:', msg)
                except Exception as e:
                     print('error:',e)
                     conn.send(data)
            else:
                 print('closing:', conn, 'data:', data)
                 self.sel.unregister(conn)
                 conn.close()
        except ConnectionResetError:
            print('client error,closing.', conn)
            self.sel.unregister(conn)
            conn.close()

    def download(self,conn):
        f = self.down_dict[conn]["rfd"]
        f.seek(self.down_dict[conn]["send_size"])
        try:
            while self.down_dict[conn]["send_size"] < self.down_dict[conn]["filesize"]:
                for line in f:
                    sendsize = conn.send(line)  ####这步非常重要，sendsize不一定等于len(line)
                    self.down_dict[conn]["send_size"] += sendsize
                if self.down_dict[conn]["send_size"] == self.down_dict[conn]["filesize"]:
                    f.close()
                    del self.down_dict[conn]
                    print("sending complete!")
                    self.sel.modify(conn, selectors.EVENT_READ, self.read)
                    break
        except BlockingIOError:
            return

    def dir(self,conn):
        path = os.getcwd()
        conn.send(path.encode('utf-8'))
        self.sel.modify(conn, selectors.EVENT_READ, self.read)

    def updata(self,conn):
        f = self.up_dict[conn]["wfd"]
        f.seek(self.up_dict[conn]["get_size"])
        #print(get_size)
        try:
            while self.up_dict[conn]["filesize"] > self.up_dict[conn]["get_size"]:
                if self.up_dict[conn]["filesize"] - self.up_dict[conn]["get_size"] > 1024:
                    n = 1024
                else:
                    n = self.up_dict[conn]["filesize"] - self.up_dict[conn]["get_size"]
                r_data = conn.recv(n)
                f.write(r_data)
                self.up_dict[conn]["get_size"] += len(r_data)
                print(self.up_dict[conn]["get_size"])
            print('recieved ok')
        except BlockingIOError:
            return
if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('localhost',8899))
    s = FTPserver(sock)
    s.start()
