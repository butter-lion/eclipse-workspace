'''
Created on 2018年5月28日

@author: zhang
'''

import redis

r = redis.Redis(host='localhost', port=6379)
r.set('foo', 'Bar')
print(r.get('foo'))