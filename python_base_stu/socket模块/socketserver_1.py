'''
Created on 2018年5月16日

@author: zhang
'''

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print('{} wrote:'.format(self.client_address[0]))
                print(self.data)
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print('出错了',e)
                break

if __name__ == '__main__':
    HOST,PORT = 'localhost' , 9000
    #creat the server,blinding to localhost on port
    server = socketserver.TCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()
