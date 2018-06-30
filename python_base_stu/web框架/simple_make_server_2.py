'''
@author   : zhang
@time     : 2018-6-14 9:36
@file     :simple_make_server_2.py  
@software :PyCharm
'''

from wsgiref.simple_server import make_server


def handle_index():
    return [b'<h1>hello world! index</h1>']


def handle_date():
    return [b'<h1>hello world! date</h1>']


def RunServer(environ, start_response):
    # environ 客户端发来的所有数据
    # start_response 封装要返回给用户的数据和响应头
    start_response('200 OK',[('Content-Type', 'text/html')])
    current_url = environ['PATH_INFO']
    print(environ)
    if current_url =='/':
        return [b'<h1>hello world</h1>']
    if current_url =='/index':
        return handle_index()
    if current_url =='/date':
        return handle_date()
    else:
        return [b'<h1>404!</h1>']


if __name__ == '__main__':
    server = make_server('localhost',8000,RunServer)
    print('Servering HTTP in port 8000...')
    server.serve_forever()