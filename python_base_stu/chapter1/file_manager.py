'''
Created on 2018年4月24日

@author: zhang
'''
def find(str):
    with open ('chart.txt','r') as f:
        for line in f:
            if str in line and line.startswith('backend'):
                break
        for lines in f:
            print(lines)
            if 'backend' in lines:
                break

#str = input('please enter your http:')      
#find(str)
                
                
                
                
def add(str3):
    with open ('chart.txt','a') as f:
        f.write('\n')
        str3 = eval(str3)
        print (str3)
        for key1 in str3:
            if key1 == 'record':
                f.write('       ')
                for k in str3[key1]:
                    f.write(str(k)+' '+str(str3[key1][k]) +' ')
                f.write('\n')
            else:    
                f.write(str(key1) + ' ' +str(str3[key1]+'\n'))
str1 = {
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }

add(str(str1))