'''
Created on 2018年4月5日

@author: zhang
'''
import requests

class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        response = requests.post(url,headers=headers,allow_redirects=False)
        response.encoding = 'utf-8'
        
        if response.status_code != 200:
            return None
        
        return response.text
    
    



