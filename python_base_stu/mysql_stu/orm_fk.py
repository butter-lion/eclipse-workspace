'''
Created on 2018年5月31日

@author: zhang
'''

import sqlalchemy
from sqlalchemy import create_engine, DATE,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker,relationship
#创建链接
engine = create_engine("mysql+pymysql://root:123456@localhost/education",
                       encoding='utf-8')

Base = declarative_base()  # 生成orm基类


class Student(Base):
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)

    def __repr__(self):
        return "<User(id='%s',  name='%s')>" % (
            self.id,self.name)

class StudyRecord(Base):
    __tablename__ = 'studyrecord'  # 表名
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer,ForeignKey('student.id'))

    student = relationship('Student', backref = 'my_study_record')

    def __repr__(self):
        return "<%s(day='%s',  status='%s')>" % (self.student.name,
            self.day,self.status)

if __name__ == '__main__':
    #创建表
    Base.metadata.create_all(engine)  # 创建表结构
    #
    Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    Session = Session_class()  # 生成session实例
    #
    # user_obj = Student(name="alex", register_date="2012-02-03")  # 生成你要创建的数据对象
    # user_obj2 = Student(name="zhang", register_date="2013-02-03")
    # user_obj3 = Student(name="xiaogang", register_date="2014-02-03")
    # user_obj4 = Student(name="xiaoli", register_date="2015-02-03")
    # study_obj1 = StudyRecord(day = 1, status = 'YES', stu_id = 1)
    # study_obj2 = StudyRecord(day = 2, status = 'NO', stu_id = 3)
    # study_obj3 = StudyRecord(day = 3, status = 'YES', stu_id = 1)
    # study_obj4 = StudyRecord(day = 1, status = 'YES', stu_id = 2)
    # Session.add_all([user_obj,user_obj2,user_obj3,user_obj4,study_obj1,study_obj2,study_obj3,study_obj4])

    # Session.commit()  # 现此才统一提交，创建数据

    obj = Session.query(Student).filter(Student.name == 'alex').first()
    print(obj.my_study_record)