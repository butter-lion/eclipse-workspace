'''
Created on 2018年5月22日

@author: zhang
'''
import os
import sys
import socket
import time
import gevent

from gevent import socket, monkey

monkey.patch_all()

def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0',port))
    s.listen(500)
    while True:
        cli,addr = s.accept()
        gevent.spawn(handle_server,cli)


def handle_server(conn):
    try:
        while True:
            data = conn.recv(1024)
            print('recv:',data)
            d = data.decode().upper()
            conn.send(d.encode('utf-8'))
            if not data:
                conn.shutdown(socket.SHUT_WR)

    except Exception as e:
        print('Error:',e)

    finally:
        conn.close()

if __name__ == '__main__':
    server(8001)