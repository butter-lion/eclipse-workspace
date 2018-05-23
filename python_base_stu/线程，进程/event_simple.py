'''
Created on 2018年5月21日

@author: zhang
'''


import threading
import time

event = threading.Event()

def lighting():
    count = 0
    event.set()
    while True:
        if count> 5 and count<10:
            event.clear()
            print('\033[41;1mred light is on ...\033[0m')
        elif count >10:
            event.set()
            print('\033[42;1mgreen light is on ...\033[0m')
            count = 0
        else:
            print('\033[42;1mgreen light is on ...\033[0m')

        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.is_set():
            print('[%s] is going...'% name)
            time.sleep(1)
        else:
            print('[%s] is waiting...'% name)
            event.wait()
            print('green light is on...')

light = threading.Thread(target=lighting,)
light.start()

car1 = threading.Thread(target=car,args=('car1',))
car1.start()