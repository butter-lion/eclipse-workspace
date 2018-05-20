'''
Created on 2018年5月10日

@author: zhang
'''

import os,sys    

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from core import education,data

def add_student():
    print("请填写学生信息：")
    student_name = input("姓名：")
    student_age = int(input('年龄：'))
    student_sex = input('性别：')
    
    print("选择学校：")
    data.print_schools()
    school_name = input("学校名：")
    school = data.get_school(school_name)
    if school == None:
        print("学校选择错误")
        return add_student()
    
    print("选择班级：")
    data.print_school_grades(school)
    grade_name = input("班级名：")
    grade = data.get_grade(grade_name)
    if grade == None:
        print("学校选择错误")
        return add_student()

    student = education.Student(student_name,student_age,student_sex,school,grade)
    school.add_student(student)
    grade.add_student(student)
    data.update_student(student)
    data.update_grade(grade)
    data.update_school(school)
    print("学生 %s 注册成功！"% student.name)

def pay_tuition():   
    print("选择学生：")
    data.print_students()
    student_name = input("学生名：")
    student = data.get_student(student_name)
    if student == None:
        print("学生选择错误")
        return pay_tuition()
    
    money =  input("请输入学费金额：")
    if not money.isdigit():
        print("输入金额不正确")
        return pay_tuition()

    student.pay_tuition(int(money))
    data.update_student(student)
    
def choose_grade():
    print("选择学生：")
    data.print_students()
    student_name = input("学生名：")
    student = data.get_student(student_name)
    if student == None:
        print("学生选择错误")
        return choose_grade()
    
    print("选择学校：")
    data.print_schools()
    school_name = input("学校名：")
    school = data.get_school(school_name)
    if school == None:
        print("学校选择错误")
        return add_student()
    
    print("选择班级：")
    data.print_school_grades(school)
    grade_name = input("班级名：")
    grade = data.get_grade(grade_name)
    if grade == None:
        print("学校选择错误")
        return add_student()
    old_grade = student.grade
    old_school = student.school
    student.choose_school(school)
    student.choose_grade(grade)
    data.update_student(student)
    data.update_grade(grade)
    data.update_grade(old_grade)
    data.update_school(school)
    data.update_school(old_school)
def show_students():
    data.print_students()
    
def show_student_info():
    print("选择学生：")
    data.print_students()
    student_name = input("学生名：")
    student = data.get_student(student_name)
    if student == None:
        print("学生选择错误")
        return choose_grade()
    
    student.show_info()
    
def student_server():
    while True:
        print("学生视图：")
        print("=" * 20)
        print("1.注册学生\n2.交学费\n3.选择课程\n4.查看学生\n"
              "5.查看明细\n0.退出")
        res = input("输入序号：")
        if res == "1":
            add_student()
        elif res == "2":
            pay_tuition()
        elif res == "3":
            choose_grade()
        elif res == "4":
            show_students()
        elif res == "5":
            show_student_info()
        elif res == "0":
            print("退出成功！")
            break
        else:
            print("请选择正确的编号")
            
if __name__ == '__main__':
    student_server()