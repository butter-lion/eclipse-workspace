'''
@author   : zhang
@time     : 2018-6-14 9:22
@file     :simple_socket.py  
@software :PyCharm
'''

import socket


def handle_request(client):
    buf = client.recv(1024)
    client.send(b'HTTP/1.1 200 OK\r\n\r\n')
    client.send(b'<h1>hello world!</h1>')

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8000))
    sock.listen(5)

    while True:
        conn,addr = sock.accept()
        handle_request(conn)
        print(conn,addr)
        conn.close()


if __name__ == '__main__':
    main()