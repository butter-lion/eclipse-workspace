'''
Created on 2018年4月27日

@author: zhang
'''
import os,sys
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
#上货入口，保存到本地
def add_goods():
    with open ('../database/goods.json','r+',encoding = 'UTF-8') as f:
        good = input('Please enter good:')
        price = int(input('Plese enter price:'))
        g = json.load(f)
        g.append((good,price))
        f.seek(0)
        f.write(json.dumps(g))
        print('add goods success!')
        print (f)
#add_goods()
#购物入口，并添加到购物车，保存到本地文件
def shopping():
    #创建货物列表goods
    goods=[]
    #创建购物车列表
    shopping_cart=[]
    with open ('../database/goods.json','r+',encoding = 'UTF-8') as f:
        #将货物添加进列表
        goods = json.load(f)
        for i in range(len(goods)):
            h = str(i+1)
            p = str(goods[i][1])
            #打印货物列表
            print ('id:'+h+' '+goods[i][0]+' '+p)
    print('quit enter "q"')
    #进行选择购物
    while True:       
        id = input('Please enter id of you buy:')
        if id == 'q':
            break
        else:
            id =int(id)-1
            shopping_cart.append(goods[id])
    #将选择物品加入购物车，并保存到本地
    with open('../database/shopping_cart.json','w') as f:
              f.write(json.dumps(shopping_cart))
              
def balance(admin):  
    totle_money = 0
    with open('../database/shopping_cart.json','r') as f:
        buy_goods = json.load(f)
        for good in buy_goods:
            totle_money = good[1] + totle_money

               
    
            