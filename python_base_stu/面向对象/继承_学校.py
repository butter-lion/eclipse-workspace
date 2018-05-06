'''
Created on 2018年5月6日

@author: zhang
'''
from astropy.wcs.docstrings import name

class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.studens = []
        self.staffs = []
        
    def enroll(self,stu_obj):
        print('为学员%s 办理注册手续'%stu_obj.name)
        self.studens.append(stu_obj)
        
    def hire(self,staff_obj):
        print('雇佣新员工%s'%staff_obj.name)
        self.staffs.append(staff_obj)
        
class SchoolMenber(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        
    def tell(self):
        pass
    
    
class Teacher(SchoolMenber):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course
        
    def tell(self):
        print('''
        ---- info of Teacher ----
        name: %s
        age: %s
        sex: %s
        salary: %s
        course: %s
        '''%(self.name,self.age,self.sex,self.salary,self.course))
        
    def teach(self):
        print('%s is teaching course [%s]'%(self.name,self.course))
        
        
        
class Student(SchoolMenber):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade
        
    def tell(self):
        print('''
        ---- info of Student ----
        name: %s
        age: %s
        sex: %s
        stu_id: %s
        grade: %s
        '''%(self.name,self.age,self.sex,self.stu_id,self.grade))
        
    def pay_tuition(self,amount):
        print('%s is paid tuition for $%s'%(self.name,amount))
        
        
school = School('家里蹲','白河')

t1 = Teacher('zhangsan',25,'M',20000,'Linux')
t2 = Teacher('lisi',40,'F',40000,'shuxue')

s1 = Student('xiaoli',13,'M',132412,'PythonDevOps')
s2 = Student('xiaoming',16,'M',345123331,'Windows')

t1.tell()
s1.tell()

school.enroll(s1)
school.hire(t1)
school.enroll(s2)
school.hire(t2)

print(school.studens)
print(school.staffs)

school.staffs[1].teach()

s1.pay_tuition(5000)