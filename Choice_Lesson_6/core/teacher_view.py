'''
Created on 2018年5月6日

@author: zhang
'''

import os,sys    

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from core import education,data

#老师登陆
def teacher_enter():
    data.print_teachers()
    teacher_name = input('Please enter your name:')
    teacher = data.get_teacher(teacher_name)
    if teacher == None:
        print("教师选择错误")
        return
    return teacher
#添加课程
def teacher_add_grade(teacher):
    print('请选择要添加的班级：')
    data.print_school_grades(teacher.school)
    grade_name = input('请输入班级名：')
    grade = data.get_grade(grade_name)
    if grade == None:
        print("班级选择错误")
        return teacher_add_grade()
    teacher.add_grade()(grade)
    grade.teacher = teacher
    data.update_teacher(teacher)
    data.update_grade(grade)
    teacher.school.teachers[teacher.name]=teacher
    data.update_school(teacher.school)
#显示学生列表
def teacher_show_student(t):
    t.show_students()
    
#显示所教班级列表
def teacher_show_grade(t):
    t.show_grades()
    
#选择班级   
def teacher_choose_grade(teacher):

    print("选择班级：")
    data.print_teacher_grades(teacher)
    grade_name = input("班级名：")
    grade = data.get_grade(grade_name)
    if grade == None:
        print("班级选择错误")
        return

    teacher.choose_grade(grade)
    data.update_teacher(teacher)
    
#展示所选班级的学生
def teacher_show_students(teacher):
    teacher.show_students()

#给学生打分
def teacher_modify_score(teacher):    
    print("选择学生：")
    teacher.show_students()
    student_name = input("学生名：")
    student = data.get_student(student_name)
    if student == None:
        print("学生选择错误")
        return

    score = input("请输入分数：")
    if not score.isdigit() or 0 > int(score) or int(score) > 100:
        print("输入分数不正确")
        return

    teacher.modify_score(student, score)
    data.update_teacher(teacher)
    data.update_student(student)
    data.update_grade(teacher.grade)
    print("%s 的成绩修改为: %s" % (student.name, data.get_student(student_name).score))
    
def teacher_server():
    print("教师视图：")
    print("=" * 20)
    while True:
        t = teacher_enter()
        if t == None:
            return
        else:
            print('请选择班级')
            teacher_choose_grade(t)
            print("1.查看学生\n2.修改成绩\n"
              "0.退出")
        res = input("输入序号：")

        if res == "1":
            teacher_show_students(t)
        elif res == "2":
            teacher_modify_score(t)
        elif res == "0":
            print("退出成功！")
            break
        else:
            print("请选择正确的编号")
        b = input('按任意键继续，退出请按"0":')
        if b =='0':
            break
if __name__ == '__main__':
    teacher_server()
