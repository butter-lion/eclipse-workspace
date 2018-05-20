'''
Created on 2018年5月11日

@author: zhang
'''

class animal(object):
    name = '骨傲天'
    def __init__(self,name,age):
        self.name = name
        self.age = age
       
    def worf(self):
        print('wangwangwang')
        
    #静态方法   
    @staticmethod   
    def eat(self):
        print('%s is eating!'%self.name)
    
    #类方法    
    @classmethod   
    def say(self):
        print('%s is my name!'%self.name)
        
    #属性方法
    @property
    def drink(self):    
        print('%s is drink water!'%self.name)
class Dog(animal):
    def __init__(self,name,age,size):
        super(Dog,self).__init__(name, age)
        self.size = size
        
d1 = Dog('ming',3,12)
d2 = Dog('haha',2,4)
d1.worf()
d1.eat(d2)
d1.say()
d1.drink