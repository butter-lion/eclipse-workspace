'''
@author   : zhang
@time     : 2018-6-25 8:50
@file     :urls.py  
@software :PyCharm
'''


from django.urls import path
from django.shortcuts import HttpResponse
from mainpage import views


def home(request):
    return HttpResponse('<h1>home</h1>')


urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    ]