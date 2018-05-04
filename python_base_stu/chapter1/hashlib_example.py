'''
Created on 2018年5月3日

@author: zhang
'''
import hashlib
'''
m = hashlib.md5()

m.update(b'hello !')
print(m.hexdigest())
m.update(b'It is me!')
print(m.hexdigest())

m2 = hashlib.md5()
m2.update(b'hello !It is me!')
print(m2.hexdigest())
'''
import hmac
h = hmac.new(b'12345','你是 250'.encode(encoding='utf_8', errors='strict'))
print(h.digest())
print(h.hexdigest())