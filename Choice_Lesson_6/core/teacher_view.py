'''
Created on 2018年5月6日

@author: zhang
'''
    
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
    