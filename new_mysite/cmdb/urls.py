"""new_mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.shortcuts import HttpResponse
from cmdb import views


def home(request):
    return HttpResponse('<h1>home</h1>')


urlpatterns = [
    path('home/', home),
    path('login/',views.login),
    path('userlist/',views.userlist),
    path('data_page/',views.data_page),
    path('user_login/',views.user_login),
    path('day19/',views.day19),
    path(r'datail-<int:name>.html',views.datail),
    path(r'state/',views.states),
    path(r'adduser/',views.adduser),
    path(r'state-<int:uid>/',views.state),
    path(r'del-<int:uid>/',views.userdel),
    path(r'edit-<int:uid>/',views.useredit),
    path(r'group/',views.group),
    path(r'group-<int:uid>/',views.groupminute),
    path(r'addgroup/',views.addgroup),
    path(r'groupdel-<int:uid>/',views.groupdel),
    path(r'groupedit-<int:uid>/',views.groupedit),
    path(r'host/',views.host),
    path(r'test_ajax/',views.test_ajax),
    path(r'manytomany/',views.manyto),
    path(r'test1/',views.test1),
    path(r'test2_page/',views.test2),
]
