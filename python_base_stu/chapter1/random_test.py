'''
Created on 2018年5月3日

@author: zhang
'''
import random

checkcode = ''

for i in range(4):
    current = random.randint(0,3)
    if current == i:
        
        tmp=chr(random.randint(65,90))
    else:
        tmp = random.randint(0,9)
        
    checkcode += str(tmp)
print (checkcode)
