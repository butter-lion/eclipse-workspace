'''
@author   : zhang
@time     : 2018-6-16 9:04
@file     :pymysql_test.py  
@software :PyCharm
'''

import pymysql


conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='management')

cursor = conn.cursor()
sql = 'select * from user where name="zhang"'

cursor.execute(sql)
a = cursor.fetchone()
print(a)

cursor.close()
conn.close()