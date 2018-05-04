'''
Created on 2018年4月24日

@author: zhang
'''
import time

def use_times(fun):
    def calu(*argv,**kw):
        date_start = time.time()
        fun(*argv,**kw)
        date_end = time.time()
        print('use time ',date_end - date_start)
    return calu



@use_times
def hello():
    print('hello world!')
    time.sleep(3)
    
def use_time(funcl):
    date_start = time.time()
    funcl()
    date_end = time.time()
    print('use time ',date_end - date_start)
    
    
hello()