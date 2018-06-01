'''
Created on 2018年5月31日

@author: zhang
'''

from student_manager_12.datadb import initdata

class Teacher(object):
    def __init__(self,name):
        self.name = name

    #创建班级
    def create_grade(self,grade_name):
        t = initdata.add_grade(grade_name)
        if not t:
            return('创建失败')
        else:
            return('创建成功')

    #往班级添加学生
    def join_grade(self,grade_name,stu_qq):
        initdata.enter_grade(grade_name,stu_qq)


    #上课并记录
    def teaching(self,grade_name,date):
        t = initdata.teaching_grade(self.name,grade_name,date)
        if not t:
            return
        else:
            print(t)

    #查询班级成员
    def search_syudents(self,grade_name):
        initdata.show_grade_student(grade_name)

    #查询自己讲的课
    def search_grades(self,):
        initdata.show_teaching_grades(self.name)

    #修改作业
    def give_score(self,grade_name,date):
        initdata.enter_score(grade_name, date)



