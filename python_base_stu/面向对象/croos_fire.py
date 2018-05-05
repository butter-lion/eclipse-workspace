'''
Created on 2018年5月5日

@author: zhang
'''
class animal():
    def __init__(self,name,species,sex,age):
        self.name = name
        self.species = species
        self.sex = sex
        self.age = age
        
    def boulk(self):
        print ("%s say:  wang wang wang!" %self.name)
        

a = animal('adai','dog','male',3 )

a.boulk()

print(a.age)