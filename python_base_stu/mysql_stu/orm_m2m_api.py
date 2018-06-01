'''
Created on 2018年5月22日

@author: zhang
'''
from sqlalchemy.orm import sessionmaker

from python_base_stu.mysql_stu import orm_m2m

Session_class = sessionmaker(bind=orm_m2m.engine)
session = Session_class()

# b1 = orm_m2m.Book(name='go to global', publish_date='2012-02-02')
# b2 = orm_m2m.Book(name='learn python', publish_date='2013-03-03')
# b3 = orm_m2m.Book(name='listen music', publish_date='2014-04-04')
#
# a1 = orm_m2m.Author(name='alex')
# a2 = orm_m2m.Author(name='jack')
# a3 = orm_m2m.Author(name='xiaohua')
# #
# b1.authers = [a1, a2]
# b3.authers = [a1, a2, a3]
#
# session.add_all([a1, a2, a3, b1, b2, b3])
# session.commit()

auther_obj = session.query(orm_m2m.Author).filter(orm_m2m.Author.name == 'alex').first()
print(auther_obj.books)

book_obj = session.query(orm_m2m.Book).filter_by(id =1).first()
print(book_obj.authers)

book_obj.authers.append(auther_obj)
session.commit()

auther_obj = session.query(orm_m2m.Author).filter(orm_m2m.Author.name == 'alex').first()
print(auther_obj.books)

book_obj = session.query(orm_m2m.Book).filter_by(id =1).first()
print(book_obj.authers)