'''
Created on 2018年5月22日

@author: zhang
'''
import time

import gevent
from urllib.request import urlopen
from gevent import monkey

monkey.patch_all()

def f(url,name):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))
    with open(name,'wb') as f1:
        f1.write(data)
    print('%s is down ok' % url)

start_time = time.time()

gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/','python.html'),
    gevent.spawn(f, 'https://www.yahoo.com/','yahu.html'),
    gevent.spawn(f, 'https://github.com/','github.html'),
])
print(time.time()-start_time)