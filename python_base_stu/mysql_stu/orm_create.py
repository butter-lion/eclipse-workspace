'''
Created on 2018年5月30日

@author: zhang
'''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
#创建链接
engine = create_engine("mysql+pymysql://root:123456@localhost/helloworld",
                       encoding='utf-8')

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<User(id='%s',  name='%s')>" % (
            self.id,self.name)

class student(Base):
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    age = Column(Integer)
    gender = Column(String(32))

    def __repr__(self):
        return "<User(id='%s',  name='%s')>" % (
            self.id,self.name)

if __name__ == '__main__':
    #创建表
    Base.metadata.create_all(engine)  # 创建表结构

    #增加数据
    # Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    # Session = Session_class()  # 生成session实例
    #
    # user_obj = User(name="alex", password="alex3714")  # 生成你要创建的数据对象
    # print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
    # user_obj2 = User(name="zhang", password="zhang123")
    # user_obj3 = User(name="xiaogang", password="xiaogang123")
    # user_obj4 = User(name="xiaoli", password="xiaoli123")
    # Session.add(user_obj)
    # Session.add(user_obj2)
    # Session.add(user_obj3)
    # Session.add(user_obj4)# 把要创建的数据对象添加到这个session里， 一会统一创建
    # print(user_obj.name, user_obj.id)  # 此时也依然还没创建
    #
    # Session.commit()  # 现此才统一提交，创建数据