"""django_test URL Configuration

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
from django.contrib import admin
from django.urls import path
from django_test.views import hello, current_datetime ,hours_ahead, mysql,\
    display_meta, request_meta, method_splitter, some_page_get, some_page_post
from books.views import search
from contact.views import contact, contact_thanks
from blogs.views import blogs_list
from weibo.views import weibos_list, weibo_page, weibo_remake



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('time/', current_datetime),
    path('time/plus/<int:offset>/', hours_ahead),
    path('mysql/',mysql),
    path('display_meta/',display_meta),
    path('request_meta/',request_meta),
    path('search/',search),
    path('contact/',contact),
    path('contact/thanks/',contact_thanks),
    path('somepage/', method_splitter,{'GetFunction':some_page_get,'POSTPostFunction':some_page_post}),
    path('blogs_list/',blogs_list),
    path('weibos_list/',weibos_list),
    path('weibos_list/<int:weibo_id>/',weibo_page),
    path('weibo_remake/<int:weibo_id>/',weibo_remake)
    
]
