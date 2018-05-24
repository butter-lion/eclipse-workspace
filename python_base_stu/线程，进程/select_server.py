'''
Created on 2018年5月23日

@author: zhang
'''

import select
import socket
import queue

server = socket.socket()
server.setblocking(False)

server_addr = ('localhost',10000)

print('starting up on %s port %s' % server_addr)
server.bind(server_addr)

server.listen(500)

inputs = [server,]
outputs = []

message_queues = {}

while True:
    print("waiting for next event...")

    readable, writeable, exeptional = select.select(inputs,outputs,inputs) #如果没有任何fd就绪,那程序就会一直阻塞在这里
    for s in readable:
        if s is server:
            conn, client_addr = s.accept()
            print("new connection from", client_addr)
            conn.setblocking(False)
            inputs.append(conn)  # 为了不阻塞整个程序,我们不会立刻在这里开始接收客户端发来的数据, 把它放到inputs里, 下一次loop时,这个新连接

            # 就会被交给select去监听,如果这个连接的客户端发来了数据 ,那这个连接的fd在server端就会变成就续的,select就会把这个连接返回,返回到
            # readable 列表里,然后你就可以loop readable列表,取出这个连接,开始接收数据了, 下面就是这么干 的

            message_queues[conn] = queue.Queue()  # 接收到客户端的数据后,不立刻返回 ,暂存在队列里,以后发送

        else:  # s不是server的话,那就只能是一个 与客户端建立的连接的fd了
            # 客户端的数据过来了,在这接收
            try:
                data = s.recv(1024)
                if data:
                    print("收到来自[%s]的数据:" % s.getpeername()[0], data)
                    message_queues[s].put(data)  # 收到的数据先放到queue里,一会返回给客户端
                    if s not in outputs:
                        outputs.append(s)  # 为了不影响处理与其它客户端的连接 , 这里不立刻返回数据给客户端

            except ConnectionResetError as e:
                print("客户端断开了", s)

                if s in outputs:
                    outputs.remove(s)  # 清理已断开的连接

                inputs.remove(s)  # 清理已断开的连接

                del message_queues[s]  ##清理已断开的连接

    for s in writeable:
        try:
            next_msg = message_queues[s].get_nowait()

        except queue.Empty:
            print("client [%s]" % s.getpeername()[0], "queue is empty..")
            outputs.remove(s)

        else:
            print("sending msg to [%s]" % s.getpeername()[0], next_msg)
            s.send(next_msg.upper())

    for s in exeptional:
        print("handling exception for ", s.getpeername())
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        del message_queues[s]