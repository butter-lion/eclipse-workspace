'''
Created on 2018年5月12日

@author: zhang
'''

def bulk(self):
    print('%s is yelling!'%self.name)


class Dog():
    def __init__(self,name):
        self.name = name
        
    def eat(self):
        print('%s is eating'%self.name)
        
d = Dog('小黑')

s1 = 'eat'
s2 = 'talk'
s3 = 'bulk'
'''
choice = input('>>:')


if hasattr(d, choice):
    func = getattr(d, choice)
    func()
'''    
choice = s3 
setattr(d, choice, bulk)
func = getattr(d, choice)
func(d)
d.bulk(d)


delattr(d, choice)
func = getattr(d, choice)
func(d)