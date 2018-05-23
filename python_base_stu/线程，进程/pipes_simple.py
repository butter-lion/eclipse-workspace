'''
Created on 2018年5月22日

@author: zhang
'''

from multiprocessing import Process,Pipe

def run(conn):
    conn.send([12, None, 'man'])
    conn.send([12, None, 'man222'])
    print(conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn,child_conn = Pipe()

    p = Process(target=run,args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    parent_conn.send('你还可好')
    p.join()
