'''
Created on 2018年5月22日

@author: zhang
'''

import multiprocessing
import threading
import time


def thread_run():
    print(threading.get_ident())


def run(n):
    time.sleep(2)
    print('%s is runing'% n)
    t = threading.Thread(target=thread_run,)
    t.start()


if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run,args=(i,))
        p.start()