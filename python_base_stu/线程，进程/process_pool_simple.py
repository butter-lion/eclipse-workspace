'''
Created on 2018年5月22日

@author: zhang
'''

from multiprocessing import Process,Pool
import time
import os

def Foo(i):
    time.sleep(2)
    print('in process',os.getpid())
    return i+100

def Bar(arg):
    print('-->exec done',os.getpid())


if __name__ == '__main__':
    pool = Pool(2)
    print('主进程',os.getpid())
    for i in range(10):
        # pool.apply(func=Foo, args=(i,))  #串行
        # pool.apply_async(func=Foo,args=(i,))#并行
        pool.apply_async(func=Foo, args=(i,), callback=Bar)  # callback是回调函数，会把func函数的返回值传给callback函数，且回调函数在主程序内运行。

    print('end')
    pool.close()
    pool.join()