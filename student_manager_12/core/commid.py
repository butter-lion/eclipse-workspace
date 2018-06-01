'''
Created on 2018年6月1日

@author: zhang
'''
from student_manager_12.core import student_view,teacher_view
from student_manager_12.datadb import initdata
def teacher_views():
    #教师视图
    teacher_name = input('请输入教师姓名')
    teacher = teacher_view.Teacher(teacher_name)
    while True:
        choice = input("1.增加课程，2.增加上课记录，3.把学生增加到班级，4.修改学生成绩，5.查询班级学生")
        if choice == "1":
            grade_name = input("课程名称:")
            ret = teacher.create_grade(grade_name)
            print(ret)
        elif choice == "2":
            grade_name = input("课程名称:")
            date = input('上课时间:')
            ret = teacher.teaching(grade_name,date)
            print(ret)
        elif choice == "3":
            qq = input("请输入学生qq号：")
            grade_name = input("课程名称:")
            ret = teacher.join_grade(grade_name, qq)
            print(ret)
        elif choice == "4":
            teacher.search_grades()
            grade_name = input("课程名称:")
            date = input("上课时间：")
            teacher.give_score(grade_name, date)
        elif choice == "5":
            grade_name = input("课程名称:")
            ret = teacher.search_syudents(grade_name)
            print(ret)
        else:
            print("请输入正确的选项")


def student_views():
    student_name = input('请输入学生姓名')
    student = student_view.Student(student_name)
    while True:
        choice = input("1.选择课程，2.提交作业")
        if choice == "1":
            grade_name = input("课程名称:")
            ret = student.join_grade(grade_name)
            print(ret)
        elif choice == "2":
            student.enter_status()
        else:
            print("请输入正确的选项")

#创建学生
def create_stu():
    name = input("请输入姓名:")
    password = input('请输入密码:')
    qq = int(input('请输入qq:'))
    initdata.add_student(name, password, qq)
#创建教师
def create_tea():
    name = input("请输入姓名:")
    password = input('请输入密码:')
    initdata.add_teacher(name, password)

def main():
    role = input("选择角色：1.教师，2.学生，3.创建教师，4.创建学生")
    if role == "1":
        teacher_views()
    elif role == "2":
        student_views()
    elif role == "4":
        create_stu()
    elif role == "3":
        create_tea()
    else:
        print("输入错误，退出程序")

