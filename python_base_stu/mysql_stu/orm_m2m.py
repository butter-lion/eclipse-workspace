'''
Created on 2018年5月31日

@author: zhang
'''
from sqlalchemy import Column, DATE, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('mysql+pymysql://root:123456@localhost/education',
                       encoding = 'utf-8')

Base = declarative_base()

book_m2m_auther = Table('book_m2m_author', Base.metadata,
                        Column('book_id', Integer, ForeignKey('books.id')),
                        Column('auther_id',Integer,ForeignKey('authors.id')),
                        )


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key= True)
    name = Column(String(32), nullable= False)

    def __repr__(self):
        return self.name

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable= False)
    publish_date = Column(DATE)

    authers = relationship('Author',secondary=book_m2m_auther, backref='books')

    def __repr__(self):
        return self.name

if __name__ == '__main__':
    Base.metadata.create_all(engine)
