'''
Created on 2018年5月6日

@author: zhang
'''

import os,sys    

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from core import education,data

def teacher_enter():
    t1 = input('Please enter your name:')
    if t1 =='q':
        break
    else:
        if t1 in teachers:
            t = teachers[ti]
        else:
            print('This is a wrong name!')
            print('Quit enter "q"')
            teacher_enter()
    