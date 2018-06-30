'''
@author   : zhang
@time     : 2018-6-23 17:24
@file     :ooxx.py  
@software :PyCharm
'''


from django import template

register = template.Library()

@register.simple_tag
def haha(a1,a2):
    return (a1+a2)


@register.filter
def wulala(a1,a2):

    return (a1+a2)