'''
Created on 2018年4月25日

@author: zhang
'''

def bounce_height_recursion(h,n, rate = 0.6):
    if n == 1:
        return (h+h*0.6)
    else:
        return((h*0.6+h)+bounce_height_recursion(0.6*h, n-1))
    
    
    
if __name__ == '__main__':
    h = int(input('Please enter the height of the ball:\n'))
    n = int(input('Please enter thr bounce times of the ball:\n'))
    print(bounce_height_recursion(h, n))
