'''
Created on 2018年4月22日

@author: zhang
'''

import os
cash = 0
goods = []
with open('goods_list.txt', 'r') as f:
    for line in f:
        goods.append(line.split(','))
if os.path.isfile('wallet.txt'):
    with open('wallet.txt') as f:
        f.readline()
        cash=int(f.readline())
else:
    cash = int(input("Please enter the amount of your money:"))
print('-----goods-----')
n=1
for k in goods:
    print('id:',n," ",k[0],' ',k[1])
    n=n+1
print('quit enter "q"')
good = [] 
while True:
    id = input('please enter goods id:')
    if id == 'q':
        print('you have buy these goods')
        print(good)
        print('you have lost money ', cash)
        with open('wallet.txt','w+') as f:
            f.write('you have lost money \n')
            f.write(str(cash))
            
        break
    else:
        id1 = int(goods[int(id)-1][1])
        if cash >= id1:
            good.append(goods[int(id)-1])
            cash = cash - int(goods[int(id)-1][1])
        else:
            print("you don't have enough money")
            
        