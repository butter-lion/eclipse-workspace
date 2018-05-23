'''
Created on 2018年5月22日

@author: zhang
'''

from multiprocessing import Process,Manager
import os

def run(d,l):
    d[os.getpid()] = os.getpid()
    l.append(os.getpid())
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        dic = manager.dict()
        list = manager.list(range(5))
        dic['asd'] = 'wqqwwww'
        p_list = []
        for i in range(10):
            p = Process(target=run,args=(dic,list))
            p_list.append(p)
            p.start()

        for res in p_list:
            res.join()


        print(dic)
        print(list)
