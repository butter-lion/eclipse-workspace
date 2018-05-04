'''
Created on 2018年5月3日

@author: zhang
'''
import re
#加减计算
def jiajian(s):
    sum = 0
    #将数字和 + ，- 分散到列表
    r = re.compile(r'[\d\.]+|\+|-')
    f = re.findall(r, s)
    print('加减列表=',f)
    #处理连续的两个符号,'--'
    for i in range(len(f)):
        if f[i] == '-' and f[i+1]=='-':
            
            f[i]='+'
            f[i+1] = '+'  
    #处理 - 号 
    for j in range(len(f)):
        if f[j] =='-':
            f[j] = '+'
            f[j+1] = float(f[j+1])*-1
    #数组内数字相加
    for i in f:
        if i == '+':
            i = 0
        #结果累加
        sum += float(i)
        print('加减结果=',sum)
    return str(sum)   

#进行乘除计算
def chengchu(s):
    r = re.compile(r'[\d\.]+[\*/]-?[\d\.]+')
    while re.search(r'[\*/]', s):
    #处理乘除
        ma = re.search(r, s).group()
        li = re.findall('-?[\d\.]+|\*|/', ma)
        print('乘除列表=',li)
        if li[1] == '*':
            result = str(float(li[0])*float(li[2]))
        else:
            result = str(float(li[0])/float(li[2]))
        print('乘除结果=',result)
        s = s.replace(ma,result)
        print (s)
    return s
        
#处理没有括号的        
def simple(s):
    return jiajian(chengchu(s))
#处理有括号的
def complex(s):
    while '(' in s:
        reg = re.compile(r'\([^\(\)]+\)')
        ma = re.search(reg, s).group()
        print('取括号列表=',ma)
        result = simple(ma[1:-1])
        s = s.replace(ma, result)
        print(s)
    return simple(s)

ss='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'.replace(' ', '')
print (complex(ss))
print(eval(ss))