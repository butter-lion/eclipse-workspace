'''
Created on 2018年5月22日

@author: zhang
'''

import threading
import queue
import time


def producer():
    count = 1
    while True:
        q.put("骨头%s" % count)
        print('生产出了 骨头%s' % count)
        count += 1
        time.sleep(0.5)


def consumer(n):
    while True:
        print("%s 取到" % n, q.get())
        time.sleep(2)


q = queue.Queue()

p = threading.Thread(target=producer, )
p.start()

c1 = threading.Thread(target=consumer,args=('李闯',))

c2 = threading.Thread(target=consumer,args=('lilili',))
c1.start()
c2.start()