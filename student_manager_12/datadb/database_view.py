'''
Created on 2018年5月31日

@author: zhang
'''

import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer, Table, ForeignKey, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


#创建链接
engine = create_engine('mysql+pymysql://root:123456@localhost/education?charset=utf8',
                       encoding='utf-8')

Base = declarative_base()

#班级与学生的多对多关系表
student_m2m_grade = Table('student_m2m_grade', Base.metadata,
                        Column('student_id', Integer, ForeignKey('students.id')),
                        Column('grade_id',Integer,ForeignKey('grades.id')),
                        )

#教师表
class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String(32),nullable=False)
    password = Column(String(32),nullable=False)

    def __repr__(self):
        return self.name

#学生表
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    password = Column(String(32), nullable=False)
    qq = Column(Integer)

    def __repr__(self):
        return self.name

#班级表，和学生表有一张映射表
class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)

    students = relationship('Student', secondary=student_m2m_grade, backref='grades')

    def __repr__(self):
        return self.name

#上课，成绩，打分记录表
class GradeRecord(Base):
    __tablename__ = 'grade_records'
    id = Column(Integer, primary_key=True)
    grade_id = Column(Integer, ForeignKey("grades.id"))
    stu_id = Column(Integer, ForeignKey("students.id"))
    date = Column(DATE)
    task_status = Column(String(64))
    score = Column(Integer, default= 0 )

    grade = relationship("Grade", foreign_keys=[grade_id], backref="grade_records")
    student = relationship("Student", foreign_keys=[stu_id], backref="grade_records")

    def __repr__(self):
        return "%s | %s | %s | %s | %s | %s" % (
            self.id, self.grade.name, self.student.name,
            self.date, self.task_status, self.score)

#课程记录表
class TeachingGrade(Base):
    __tablename__ = 'teaching_grades'
    id = Column(Integer, primary_key=True)
    grade_id = Column(Integer, ForeignKey("grades.id"))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    date = Column(DATE)

    grade = relationship("Grade", foreign_keys=[grade_id], backref="teaching_grade")
    teacher = relationship("Teacher", foreign_keys=[teacher_id], backref="teaching_grade")

    def __repr__(self):
        return "%s | %s | %s | %s " % (
            self.id, self.grade.name, self.teacher.name,
            self.date)

if __name__ == '__main__':
    Base.metadata.create_all(engine)