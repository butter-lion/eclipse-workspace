'''
Created on 2018年5月22日

@author: zhang
'''

from multiprocessing import Process,Queue


def f(q):
    q.put([42, None, 'hello'])
    print('f 的 进程id',Process.ident)


if __name__ == '__main__':
    q = Queue()
    print('主进程id', Process.ident)
    p = Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()