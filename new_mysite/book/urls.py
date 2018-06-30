'''
@author   : zhang
@time     : 2018-6-25 22:26
@file     :urls.py  
@software :PyCharm
'''

from django.urls import path
from book import views



urlpatterns = [
    path('login/',views.login),
    path('books/',views.books),
    path('books_add/',views.books_add),
    path('books_del-<int:did>/',views.books_del),
    path('books_set-<int:sid>/',views.books_set),

    path('authors/',views.authors),
    path('authors_add/',views.authors_add),
    path('authors_del-<int:did>/',views.authors_del),
    path('authors_set-<int:sid>/',views.authors_set),

    path('publishers/',views.publishers),
    path('publishers_add/',views.publishers_add),
    path('publishers_del-<int:did>/',views.publishers_del),
    path('publishers_set-<int:sid>/',views.publishers_set),

    path('login/',views.login),
    path('register/',views.register.as_view()),
    path('register_ok/',views.register_ok),
]
