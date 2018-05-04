'''
Created on 2018年4月5日

@author: zhang
'''
import requests

def img_download():
    '''下载实验
    '''
    url='https://baike.baidu.com/item/Python/407313'
    respons = requests.get(url,allow_redirects=False)
    print(respons.headers)
    print(respons.status_code)
    print(respons.content)
    with open('juren.jpg','wb') as fb:
        fb.write(respons.content)
img_download()

