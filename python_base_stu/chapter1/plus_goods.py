'''
Created on 2018年4月24日

@author: zhang
'''

print('please plus goods, quit enter "q"')
while True:
    good = input('please enter you plus good:')
    if good == 'q':
        break
    price = input('please enter price:')
    with open('goods_list.txt','a') as f:
        f.write(good)
        f.write(',')
        f.write(price)
        f.write('\n')