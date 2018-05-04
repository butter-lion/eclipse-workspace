'''
Created on 2018年4月8日

@author: zhang
'''
from django.http import HttpResponse
import datetime
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from books.models import Publisher
def hello(request):
    return HttpResponse("wellcom to the page at %s" % request.path[1:-1])
def mysql(request):
    qqq = Publisher.objects.get(name = 'Apress')
    return HttpResponse(qqq.address)
def current_datetime(requset):
    now = datetime.datetime.now()
    html = render(requset,'current_datetime.html',{'current_date': now})
    return html

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now = datetime.datetime.now()
    dt = now + datetime.timedelta(hours=offset)
    html = render(request,'hours_ahead.html',{'hour_offset':offset, 'next_time':dt})
    return html

def display_meta(request):
    values = request.META.items()
#    values.sorted()
    html = []
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
    return HttpResponse('<table>%s</table>' % ''.join(html))

def request_meta(request):
    values = request.META.items() 
    html = render(request,'request_meta.html',{'values':values})
    return html

def method_splitter(request, *args, **kwargs):
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)
    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404

def some_page_get(request):
    assert request.method == 'GET'
    return HttpResponse("welcome to some page")

def some_page_post(request):
    assert request.method == 'POST'
    return HttpResponseRedirect('/contact/thanks/')

