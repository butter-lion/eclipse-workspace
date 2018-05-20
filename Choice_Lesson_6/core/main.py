'''
Created on 2018年5月6日

@author: zhang
'''

import os,sys    

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from core import teacher_view, student_view, manage_view

def run_server():
    while True:
        print("主界面：")
        print("=" * 20)
        print("1.学生模块\n2.教师模块\n3.管理模块\n0.退出")
        res = input("输入序号：")
        if res == "1": 
            student_view.student_server()
        elif res == "2":
            teacher_view.teacher_server()
        elif res == "3":
            manage_view.manage_server()
        elif res == "0":
            print("退出成功！")
            break
        else:
            print("请选择正确的编号")
