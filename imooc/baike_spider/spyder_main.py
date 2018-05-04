'''
Created on 2018年4月5日

@author: zhang
'''
from baike_spider import html_outputer, url_manager, html_downloader,\
    html_parser



class SpiderMain(object):
    def __init__(self):
        #url 管理器，检查是否有新的url，获取url，向url库里注入新的url，检查url是否被爬取过
        self.urls = url_manager.UrlManager()
        #页面下载器，把新的url的页面信息下载下来
        self.downloader = html_downloader.HtmlDownloader()
        #页面处理器，把获取到的页面进行分析，取得需要的信息
        self.parser = html_parser.HtmlParser()
        #信息下载，吧获取到的信息注入数据库
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url ,number):
        num = 1
        scount = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            count = 1
            while self.urls.has_new_url():
                try:
                    #从页面管理器取得新的url
                    new_url = self.urls.get_new_url()
                    #对页面信息进行下载
                    html_cont =self.downloader.download(new_url)
                    #对获取的页面进行分析，获取url的地址和所需的页面数据
                    new_urls,new_data =self.parser.parse(new_url,html_cont)
                    #向url库里注入新的url
                    self.urls.add_new_urls(new_urls)
                    #将获取到的信息注入数据库内
                    self.outputer.collect_data(new_data)
                   
                    print('craw:',num,'      ',new_url)
                    #每注入十条数据，对数据库进行一次写入，并清空一次缓存datas
                    if count == 10 or num == number:
                        num = num + 1
                        break
                    count =count + 1
                    num = num + 1
                except Exception as e:
                    print('Error:',scount,'       has error')
                    scount = scount + 1
            #数据库写入操作
            self.outputer.outpu_html()
            #当获取所需数量的页面信息时，break操作，结束程序
            if num == number + 1:
                print('Success craw ',number,' pages')
                print('Error:',scount,' pages have error')
                print(self.urls.get_news_url_len())
                print(self.urls.get_olds_url_len())
                break
            
            
            
    
    



if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url,35)
    
    
    