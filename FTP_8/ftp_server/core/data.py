'''
Created on 2018年5月17日

@author: zhang
'''


import json
import os,sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = (BASE_PATH + '\data\data.json')


# 写入
def dump(obj):
    f = open(path, "w")
    json.dump(obj, f)
    f.close()


# 读取所有数据
def loads():
    f = open(path, "r")
    infos = json.load(f)
    f.close()
    return infos

#读取某人数据
def load(username):
    f = open(path, "r")
    infos = json.load(f)
    f.close()
    return infos[username]


# 打印所有数据
def print_all_infos():
    infos = loads()
    print("=" * 50)
    for key in infos:
        print(key, ":")
        for key2 in infos.get(key):
            print("\t", key2, ":", infos.get(key).get(key2))
    print("=" * 50)

def init():
    # 存储结构：
    infos = {
        "xiaoming": {
            'username': 'xiaoming',
            'password': '123456',
            'datapath': 'C:/Users/zhang/Desktop/eclipse-workspace/FTP_8/ftp_server/data/xiaoming',
            'datasize': 0,
            'maxsize': 1024000
        },
        "xiaoli": {
            'username': 'xiaoli',
            'password': '123456',
            'datapath': 'C:/Users/zhang/Desktop/eclipse-workspace/FTP_8/ftp_server/data/xiaoli',
            'datasize': 0,
            'maxsize': 1024000
        },
        "骨傲天": {
            'username': '骨傲天',
            'password': '123456',
            'datapath': 'C:/Users/zhang/Desktop/eclipse-workspace/FTP_8/ftp_server/data/骨傲天',
            'datasize': 0,
            'maxsize': 1024000
        },
    }
    # 初始化数据
    res = input("是否初始化数据？（y）:")
    if res == "y":
        dump(infos)
        print("数据初始化成功！")
    else:
        print("数据初始化失败！")
if __name__ == '__main__':
    init()
    print(loads())