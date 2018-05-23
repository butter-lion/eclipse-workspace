'''
Created on 2018年5月22日

@author: zhang
'''

import queue

#可设立优先级
q = queue.PriorityQueue()

q.put((10,'cheronghau'))
q.put((2,'Alex'))
q.put((-3,'ajsjkdl'))

print(q.get())
print(q.get())
print(q.get())










# 后进先出
# q = queue.LifoQueue()
#
# q.put(1)
# q.put(2)
# q.put(3)
#
# print(q.get())
# print(q.get())
# print(q.get())




#先进先出
# q = queue.Queue()
#
# q.put(1)
# q.put(2)
# q.put(3)
#
# print(q.get())
# print(q.get())
# print(q.get())