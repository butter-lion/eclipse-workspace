'''
Created on 2018年5月22日

@author: zhang
'''

import gevent

def Foo():
    print('fist run Foo')
    gevent.sleep(2)
    print('Foo is run end')


def func():
    print('fist run func')
    gevent.sleep(1)
    print('func is run end')


def server():
    print('fist run server')
    gevent.sleep(1.5)
    print('server is run end')


gevent.joinall([
    gevent.spawn(Foo),
    gevent.spawn(func),
    gevent.spawn(server)
    ])