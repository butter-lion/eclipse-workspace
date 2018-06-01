'''
Created on 2018年5月22日

@author: zhang
'''

from student_manager_12.datadb import initdata


class Student(object):
    def __init__(self, name):
        self.name = name
        self.qq = initdata.get_qq(self.name)

    #提交作业
    def enter_status(self):
        initdata.show_stu_grades(self.name)
        grade = input('请输入课程名：')
        date = input('请输入上课时间')
        status = input('请输入你的作业')
        initdata.enter_status(grade,date,status)

    #加入班级
    def join_grade(self,grade_name):
        initdata.enter_grade(grade_name,self.qq)


