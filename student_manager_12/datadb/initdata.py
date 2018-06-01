'''
Created on 2018年5月31日

@author: zhang
'''

from student_manager_12.datadb import database_view

from sqlalchemy.orm import sessionmaker

#创建Session类
Session_class = sessionmaker(bind=database_view.engine)
Session = Session_class()

#注册学生
def add_student(name, password, qq):
    stu_obj = database_view.Student(name=name, password=password, qq=qq)
    Session.add(stu_obj)
    Session.commit()
    print ('student create access!')
#注册教师
def add_teacher(name, password):
    try:
        tea_obj = database_view.Teacher(name=name, password=password)
        Session.add(tea_obj)
        Session.commit()
        print('teacher create access!')
    except Exception as e:
        print(e)

#创建班级
def add_grade(name):
    try:
        geade_obj = database_view.Grade(name=name)
        Session.add(geade_obj)
        Session.commit()
        return ('grade create access!')
    except Exception as e:
        print(e)
        return

#展示班级学员
def show_grade_student(grade_name):
    grade_obj = Session.query(database_view.Grade).filter_by(name = grade_name).first()
    for stu in grade_obj.students:
        print(stu.name)

#学员加入班级
def enter_grade(grade_name,qq):
    stu_obj = Session.query(database_view.Student).filter_by(qq = qq).first()
    grade_obj = Session.query(database_view.Grade).filter_by(name=grade_name).first()
    grade_obj.students.append(stu_obj)
    Session.commit()
    print(stu_obj.name ,'进入了',grade_obj.name)

#教师上课
def teaching_grade(teacher_name,grade_name,date):
    teacher_obj = Session.query(database_view.Teacher).filter_by(name=teacher_name).first()
    grade_obj = Session.query(database_view.Grade).filter_by(name=grade_name).first()
    teaching_date = date
    teaching_grade_obj = database_view.TeachingGrade(teacher = teacher_obj, grade = grade_obj, date=teaching_date)
    Session.add(teaching_grade_obj)
    for stu_obj in grade_obj.students:
        graderecord_obj = database_view.GradeRecord(grade = grade_obj, student = stu_obj, date = teaching_date)
        Session.add(graderecord_obj)
    Session.commit()
    print('grade create access!')

#展示教师课程
def show_teaching_grades(teacher_name):
    teacher = Session.query(database_view.Teacher).filter_by(name = teacher_name).first()
    print(teacher.teaching_grade)

#教师指定课程,打分
def enter_score(grade_name,date):
    grade_obj = Session.query(database_view.Grade).filter_by(name=grade_name).first()
    grade_record_objs = Session.query(database_view.GradeRecord).filter(database_view.GradeRecord.grade == grade_obj).filter(database_view.GradeRecord.date == date)
    for obj in grade_record_objs:
        print('给%s打分' % obj.student.name)
        score = input('请输入分数')
        obj.score = int(score)
    Session.commit()
    print('打分完成')

#展示学生课程
def show_stu_grades(stu_name):
    stu_obj = Session.query(database_view.Student).filter_by(name=stu_name).first()
    print(stu_obj.grade_records)

#获取qq
def get_qq(stu_name):
    stu_obj = Session.query(database_view.Student).filter_by(name = stu_name).first()
    return stu_obj.qq

#学生选择课程提交作业
def enter_status(grade_name,date,status):
    grade_obj = Session.query(database_view.Grade).filter_by(name=grade_name).first()
    obj = Session.query(database_view.GradeRecord).filter_by(grade=grade_obj).filter_by(date=date).first()
    obj.task_status = status
    Session.commit()

if __name__ == '__main__':
    name = 'zhang'
    password = '123456'
    qq =12345678
    add_student(name,password,qq)