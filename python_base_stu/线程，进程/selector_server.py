'''
Created on 2018年5月23日

@author: zhang
'''
import selectors
import socket
import json, os


class FtpServer(object):
    def __init__(self, sock):
        '''
        :param upload_dict 用于存放上传文件状态信息参数，在read()中有详细说明
        :param download_dict 用于存放下载文件状态信息参数，在read()中有详细说明
        '''
        self.sel = selectors.DefaultSelector()
        self.sock = sock
        self.upload_dict = {}
        self.download_dict = {}

    def start(self):
        '''
        :param key.data 指的是调用的方法
        :param key.fileobj  指的是传入的sock
        :param mask 无引用或指向，无实际意义。
        '''
        self.sock.listen(10)
        self.sock.setblocking(False)
        self.sel.register(sock, selectors.EVENT_READ, self.accept)
        while True:
            events = self.sel.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj)

    def accept(self, sock):
        conn, addr = sock.accept()
        print('accepted', conn, 'from', addr)
        conn.setblocking(False)
        self.sel.register(conn, selectors.EVENT_READ, self.read)

    def read(self, conn):
        '''
        判断输入的命令，然后将sock状态设置为读或写，直到任务结束再由任务自己调整回来
        将文件读写open操作放在这里，是为了避免因BlockingIOError多次打开和关闭文件
        :param  upload_dict = {conn:{   "motion": "put",
                                        "filename": filename,
                                        "filesize":0,
                                        "md5":md5,
                                        "recv_size":recv_size,      已接收的字节数
                                        "wfd":fd                    打开用于写入的文件句柄
                                        }}

        :param download_dict = {conn:{   "motion": "get",
                                        "filename": filename,
                                        "filesize":0,
                                        "md5":md5,
                                        "send_size":send_size,      作为传输中断后再次传输时，cursor的锚位
                                        "rfd":fd                    打开用于读的文件句柄
                                        }}
        '''
        try:
            data = conn.recv(1024)
            print("read:", conn, "data:", data)
            if data:
                try:
                    msg = json.loads(data.decode("utf-8"))
                    # print("msg:",msg,"from conn:",conn)
                    motion = msg["motion"]
                    filename = msg["filename"]

                    if "put" == motion:
                        msg["recv_size"] = 0
                        wfd = open(filename, "wb")
                        msg["wfd"] = wfd
                        self.upload_dict[conn] = msg
                        conn.send(b'ready to receive')
                        self.sel.modify(conn, selectors.EVENT_READ, self.upload)

                    elif "get" == motion:
                        filesize = os.path.getsize(filename)
                        filemd5 = 123456
                        msg["filesize"] = filesize
                        msg["md5"] = filemd5
                        print(msg)
                        conn.send(json.dumps(msg).encode("utf-8"))
                        msg["send_size"] = 0
                        rfd = open(filename, "rb")
                        msg["rfd"] = rfd
                        self.download_dict[conn] = msg
                        self.sel.modify(conn, selectors.EVENT_WRITE, self.download)
                    else:
                        print('func matching miss:', msg)
                except Exception as e:
                    print('error:', e)
                    conn.send(data)
            else:
                print('closing:', conn, 'data:', data)
                self.sel.unregister(conn)
                conn.close()
        except ConnectionResetError:
            print('client error,closing.', conn)
            self.sel.unregister(conn)
            conn.close()

    def upload(self, conn):
        '''
        非阻塞模式下，server在遇到等待，就会直接报出BlockingIOError: [Errno 11] Resource temporarily unavailable，利用该报错退出当前任务
        文件在writing的过程中可能会因BlockingIOError中断多次，每次中断时都将当期状态信息保存在upload_dict中
        '''
        filename = self.upload_dict[conn]["filename"]
        filesize = self.upload_dict[conn]["filesize"]
        f = self.upload_dict[conn]["wfd"]
        recv_size = self.upload_dict[conn]["recv_size"]
        while filesize > recv_size:
            if filesize - recv_size > 1024:
                n = 1024
            else:
                n = filesize - recv_size
            try:
                r_data = conn.recv(n)
                f.write(r_data)
                recv_size += len(r_data)
                self.upload_dict[conn]["recv_size"] = recv_size
                if filesize == recv_size:
                    f.close()
                    filemd5 = 123456
                    print("receive complete! filename:", filename, "filesize", filesize, "recv_filemd5:", filemd5,
                          "original_filemd5:", self.upload_dict[conn]["md5"])
                    del self.upload_dict[conn]
                    self.sel.modify(conn, selectors.EVENT_READ, self.read)
            except BlockingIOError:
                break

    def download(self, conn):
        '''
        non-blocking模式下，发送一旦遇到exception，send操作可能只发送部分数据出去，不能用len(line)来统计发送的字节数，即使是放在send之后统计
        :param sendsize 发送出去的数据字节
        :return 遇到IO等待事件，让出队列，让其他任务执行
        :exception BlockingIOError  IO遇到堵塞报的错，退出当前任务
        :exception ConnectionResetError 客户端断开连接报的错，执行收尾工作
        '''
        f = self.download_dict[conn]["rfd"]
        f.seek(self.download_dict[conn]["send_size"])
        try:
            while self.download_dict[conn]["send_size"] < self.download_dict[conn]["filesize"]:
                for line in f:
                    sendsize = conn.send(line)  ####这步非常重要，sendsize不一定等于len(line)
                    self.download_dict[conn]["send_size"] += sendsize

                if self.download_dict[conn]["send_size"] == self.download_dict[conn]["filesize"]:
                    f.close()
                    del self.download_dict[conn]
                    print("sending complete!")
                    self.sel.modify(conn, selectors.EVENT_READ, self.read)
                    break
        except BlockingIOError:
            return
        # except ConnectionResetError:
        #     print("lose connection:",conn)
        #     f.close()
        #     del self.download_dict[conn]
        #     self.sel.modify(conn, selectors.EVENT_READ, self.read)


if __name__ == "__main__":
    sock = socket.socket()
    sock.bind(('0.0.0.0', 9999))
    s = FtpServer(sock)
    s.start()