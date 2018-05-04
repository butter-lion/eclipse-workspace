'''
Created on 2018年5月3日

@author: zhang
'''
import configparser

conf = configparser.ConfigParser()
conf.read('configparser_example.ini', encoding='utf-8')
print(conf.sections())
print(conf.defaults())
print(conf['topsecret.server.com']['host port'])
for key in conf['topsecret.server.com']:
    print(key)
    
print(conf['topsecret.server.com']['serveraliveinterval'])