'''
Created on 2018年5月6日

@author: zhang
'''

import os,sys    

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from core import education,data
    
# 创建学校
def add_school():
    print("请填写学校信息：")
    school_name = input("名称：")
    address = input("地址：")
    school = education.School(school_name, address)
    data.update_school(school)
    print("学校 %s 创建成功！"% school.name)
#创建班级
def add_grade():
    print("请填写班级信息：")
    grade_name = input("名称：")
    
    print('请选择学校：')
    data.print_schools()
    school_name = input('学校名：')
    school = data.get_school(school_name)
    if school == None:
        print("学校选择错误")
        return add_grade()
    
    print('请选择教师：')
    data.print_school_teachers(school)
    teacher_name = input('教师名：')
    teacher = data.get_teacher(teacher_name)
    if teacher == None:
        print("教师选择错误")
        return add_grade()
    
    print('请选择课程：')
    data.print_school_courses(school)
    course_name = input('课程名：')
    course = data.get_course(course_name)
    if course == None:
        print("课程选择错误")
        return add_grade()
    #生成Grade对象
    grade= education.Grade(grade_name, course, teacher)
    #将新建Grade添加进school
    grade.teacher.grades.append(grade)
    school.add_grades(grade)
    #更新grade和school列表
    data.update_teacher(grade.teacher)
    data.update_grade(grade)
    data.update_school(school)
    print("班级 %s 创建成功！"% grade.name)
#创建课程    
def add_course():
    print("请填写课程信息：")
    course_name = input("名称：")
    time = input("周期：")
    price = input("学费：")

    print("选择学校：")
    data.print_schools()
    school_name = input("学校名：")
    school = data.get_school(school_name)
    if school == None:
        print("学校选择错误")
        return add_course()
    
    course = education.Course(course_name, time, price)
    school.add_course(course)
    data.update_course(course)
    data.update_school(school)    
    print("课程 %s 创建成功！"% course.name)
# 创建老师
def add_teacher():
    print("请填写教师信息：")
    teacher_name = input("姓名：")
    teacher_age = int(input('年龄：'))
    teacher_sex = input('性别：')
    
    print("选择学校：")
    data.print_schools()
    school_name = input("学校名：")
    school = data.get_school(school_name)
    if school == None:
        print("学校选择错误")
        return add_teacher()
    
    teacher = education.Teacher(teacher_name,teacher_age,teacher_sex,school)
    school.add_teacher(teacher)
    for t in school.teachers:
        t.school = school
        data.update_teacher(t)
    data.update_school(school)
    print("老师 %s 创建成功！"% teacher.name)
    
def show_schools():
    data.print_schools()

def show_courses():
    data.print_courses()

def show_teachers():
    data.print_teachers()

def show_grades():
    data.print_grades()

def show_teacher():
    print("选择老师：")
    data.print_teachers()
    teacher_name = input("老师名：")
    teacher = data.get_teacher(teacher_name)
    if teacher == None:
        print("老师选择错误")
        return

    teacher.show_info()

def show_grade():
    print("选择课程：")
    data.print_grades()
    grade_name = input("课程名：")
    grade = data.get_grade(grade_name)
    if grade == None:
        print("老师选择错误")
        return

    grade.show_info()
    

def show_school():
    print('选择学校：')
    data.print_schools()
    school_name = input("学校名：")
    school = data.get_school(school_name)
    if school == None:
        print("学校选择错误")
        return
    school.show_info()
    
def manage_server():
    while True:
        print("管理视图：")
        print("=" * 20)
        print("1.增加学校\n2.增加老师\n3.增加课程\n4.增加班级\n"
              "5.查看学校\n6.查看老师\n7.查看课程\n8.查看班级\n"
              "9.查看教师详细\n10.查看班级详细\n11.查看学校详细\n"
              "0.退出")
        res = input("输入序号：")

        if res == "1":
            add_school()
        elif res == "2":
            add_teacher()
        elif res == "3":
            add_course()
        elif res == "4":
            add_grade()
        elif res == "5":
            show_schools()
        elif res == "6":
            show_teachers()
        elif res == "7":
            show_courses()
        elif res == "8":
            show_grades()
        elif res == "9":
            show_teacher()
        elif res == "9":
            show_teacher()
        elif res == "10":
            show_grade()
        elif res == "11":
            show_school()
        elif res == "0":
            print("退出成功！")
            break
        else:
            print("请选择正确的编号")
            
if __name__ == '__main__':
    manage_server()