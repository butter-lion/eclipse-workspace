'''
Created on 2018年4月5日

@author: zhang
'''
import pymysql
from sqlalchemy.sql.expression import except_




class HtmlOutputer(object):
    
    
    def __init__(self):
        self.datas = []
        

    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def outpu_html(self):
        
        for data in self.datas:
            
            conn = pymysql.Connect(
                    host = '127.0.0.1',
                    port = 3306,
                    user = 'root',
                    password = '123456',
                    db = 'imooc',
                    charset = 'utf8'
                    )
            cursor = conn.cursor()
            sql_insert ="insert into baike_spider values('%s','%s','%s')" %(data['title'],data['url'],data['summary']) 

            try:
                cursor.execute(sql_insert)
                conn.commit()
            except Exception as e:
                conn.rollback()
            
            cursor.close()
            conn.close()
            
        self.datas = []



