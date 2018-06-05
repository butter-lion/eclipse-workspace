'''
Created on 2018年6月2日

@author: zhang
'''

import socket


def handle_request(client):
    buf = client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n", encoding='utf-8'))
    with open('index.html','rb') as h1:
        html = h1.read()
    client.send(html)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        print(conn,addr)
        handle_request(conn)
        conn.close()


if __name__ == '__main__':
    main()