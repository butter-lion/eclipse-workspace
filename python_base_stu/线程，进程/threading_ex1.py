'''
Created on 2018年5月21日

@author: zhang
'''

import threading
import time


def run(n):
    print('task' + n,threading.current_thread(),threading.active_count())
    time.sleep(3)
    print('task done')
time1 = time.time()
obj_1=[]
for i in range(50):
    t = threading.Thread(target=run, args=('t%s'%i,))
    obj_1.append(t)
    t.setDaemon(True)
    t.start()

# for i in obj_1:
#     i.join()

time2 =time.time()
print(time2-time1,threading.current_thread(),threading.active_count())

# run('t1')
# run('t2')