'''
Created on 2018年5月30日

@author: zhang
'''

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import orm_create

engine = create_engine("mysql+pymysql://root:123456@localhost/helloworld",
                       encoding='utf-8')

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

#增加新数据
# user_obj = orm_create.User(name="xiaohua", password="xiaohua123")
# Session.add(user_obj)
# Session.commit()

#查询数据
# my_user = Session.query(orm_create.student).filter_by(name = 'chenronghua').first()
# print(my_user.id)

#查询所有数据
# print(Session.query(orm_create.User.name,orm_create.User.id).all() )

#多条件查询
# objs = Session.query(orm_create.User).filter(orm_create.User.id>0).filter(orm_create.User.id<7).all()
# print(objs)
# for obj in objs:
#     print(obj)

#修改数据
# user= Session.query(orm_create.User).filter_by(name = 'zhang').first()
# user.name = 'zhang shuai'
# user.password = 'zhangshuai123'
# print(user)
#
# Session.commit()

#计数 名字类似'chen%'
# a = Session.query(orm_create.student).filter(orm_create.student.name.like("chen%")).count()
# print(a)

#分组
# from sqlalchemy import func
# print(Session.query(func.count(orm_create.student.name),orm_create.student.name).group_by(orm_create.student.name).all() )

#连表
# obj = Session.query(orm_create.User,orm_create.student).filter(orm_create.User.id == orm_create.student.id).all()
# print(obj)

#连表join  两张表必须有映射关系才可以
# obj = Session.query(orm_create.User).join(orm_create.student).all()
# print(obj)