'''
Created on 2018年5月6日

@author: zhang
'''

#创建School类
class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr =addr
        self.students = []
        self.teachers = []
        self.courses = []
        self.grades = []
    #注册学生    
    def add_student(self,stu_obj):
        self.students.append(stu_obj)
        print('%s enroll in %s'%(stu_obj.name,self.name))
    #学生离校    
    def del_student(self,stu_obj):
        self.students.remove(stu_obj)
        print('%s leave school from %s'%(stu_obj.name,self.name))
    #注册老师
    def add_teacher(self,tea_obj):    
        self.teachers.append(tea_obj)
        print('%s is hire successful by school %s'%(tea_obj.name,self.name))
    #解雇老师
    def del_teache(self,tea_obj):
        self.teachers.remove(tea_obj)
        print('%s is fire by school %s'%(tea_obj.name,self.name))

    #注册课程
    def add_course(self,cour_obj):   
        self.courses.append(cour_obj)
        print('%s have create lesson %s'%(self.name,cour_obj.name))
    #注册班级
    def add_grade(self,grade):    
        self.grades.append(grade)
        print('%s have create grade %s'%(self.name,grade.name))
    
#    def __str__(self):
#        return self.name
#创建Course类       
class Course(object):
    def __init__(self,name,time,price):
        self.name =name
        self.time = time
        self.price = price
        
#    def __str__(self):
#        return self.name
#创建班级        
class Grade(object):
    def __init__(self,name,course,teacher):
        self.name = name
        self.course = course
        self.teacher = teacher
        self.students = []
        
    def enroll(self, student):  # 学员注册
        self.students.append(student)
        print("%s enroll in %s " % (student.name, self.name))

    def leave_grade(self, student): # 学员离开
        self.students.remove(student)
        print("%s leave grade from %s " % (student.name, self.name))

    def show_info(self):
        print("grade:name: %s\t teacher:%s\t course:%s\t students:%s"%
              (self.name, self.teacher, self.course, self.students))
    
#    def __str__(self):
#        return self.name   
#创建人员父类
class SchoolMenber(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    
#    def __str__(self):
#        return self.name   
#创建Teacher类        
class Teacher(SchoolMenber):
    def __init__(self,name,age,sex,school):
        super(Teacher,self).__init__(name, age, sex)
        self.school = None
        self.choose_school(school)
        self.grades = []
        self.grade  = None
    
    #选择学校
    def choose_school(self,school):
        if self.school != None:
            self.school.del_teacher(self)
        self.school = school
    
    #添加班级  
    def add_grade(self,grade):
        self.grades.append(grade)
        
    #减少班级
    def del_grade(self,grade):
        self.grades.remove(grade)
        
    #显示所教班级
    def show_grades(self):
        print(self.grades)
    
    #选择班级
    def choose_grade(self,grade):
        self.grade = grade
        
    #显示所选班级学生
    def show_student(self):
        if self.grade != None:
            for student in self.grade.students:
                student.show_info()
        else:
            print("请选择班级")
    #给学生打分       
    def modify_score(self, student, score):
        student.score = score
        
    #展示老师信息
    def show_info(self):
        print("teacher:name: %s\t age: %s\t sex: %s\t school:%s\t grade:%s"%
              (self.name, self.age, self.sex, self.school, self.grade))
        
#创建Student类
def Student(SchoolMenber):
    def __init__(self,name,age,sex,school,grade,score = 0):
        super(Student,self).__init__(name,age,sex)
        self.course = []
        self.grade = None
        self.school = None
        self.tuition = 0
        self.score = score
        self.choose_school(school)
        self.choose_grade(grade)
    #学生选择学校    
    def choose_school(self,school):
        if self.school != None:
            self.shcool.del_student(self)
            school.enroll(self)
        self.school = school
    #学生选择班级    
    def choose_grade(self,grade):
        if self.grade != None:
            self.grade.del_student(self)
            grade.enroll(self)
        self.grade = grade
        
    def pay_tuition(self, money):
        self.tuition += money
    #展示学生信息
    def show_info(self):
        print("student:name: %s\t school:%s\t grade:%s\t score:%s\t tuition:%s"%
              (self.name, self.school, self.grade, self.score, self.tuition))
