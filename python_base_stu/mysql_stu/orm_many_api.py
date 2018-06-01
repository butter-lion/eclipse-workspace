'''
Created on 2018年5月31日

@author: zhang
'''

from python_base_stu.mysql_stu import orm_many_fk
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:123456@localhost/education',
                       encoding = 'utf-8')

Session_class = sessionmaker(bind= engine)
Session = Session_class()

# addr1 = orm_many_fk.Address(stree='USA', city='washendun', state='queen')
# addr2 = orm_many_fk.Address(stree='CHN', city='beijing', state='xizhimen')
# addr3 = orm_many_fk.Address(stree='HK', city='wanzai', state='tongluoxiang')
#
# # Session.add_all([addr1,addr2,addr3])
#
# custom1 = orm_many_fk.Customer(name = 'alex',billing_address=addr1,shipping_address=addr2)
# custom2 = orm_many_fk.Customer(name = 'zhang',billing_address=addr3,shipping_address=addr3)
#
# Session.add_all([custom1,custom2])
# Session.commit()

cus = Session.query(orm_many_fk.Customer).filter(orm_many_fk.Customer.name == 'alex').first()
print(cus,cus.billing_address,cus.shipping_address)



