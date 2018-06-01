'''
Created on 2018年5月31日

@author: zhang
'''
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('mysql+pymysql://root:123456@localhost/education',
                       encoding = 'utf-8')

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key= True)
    name = Column(String(32), nullable= False)

    billing_address_id =Column(Integer,ForeignKey('address.id'))
    shipping_address_id =Column(Integer,ForeignKey('address.id'))

    billing_address = relationship('Address', foreign_keys=[billing_address_id])
    shipping_address = relationship('Address', foreign_keys=[shipping_address_id])

    def __repr__(self):
        return "%s " % (self.name)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    stree = Column(String(32))
    city = Column(String(32))
    state = Column(String(32))

    def __repr__(self):
        return "%s %s %s" % (self.stree,self.city,self.state)


if __name__ == '__main__':
    Base.metadata.create_all(engine)