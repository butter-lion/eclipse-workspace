from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
import pymysql
from cmdb import models
# Create your views here.

user_list = [{'username': 'alex', 'email': 'qwee@123.com', 'gender': '男'},
            {'username': 'alex', 'email': 'qwee@123.com', 'gender': 'nv'},
            {'username': 'alex', 'email': 'qwee@123.com', 'gender': '女'}]

def user_login(request):
    #包含用户提交的所有请求

    #获取用户提交方法
    #print(request.method)
    error_msg = ''
    if request.method == 'POST':
        #获取用户POST方法提交过来的数据
        user = request.POST.get('username', None)
        pwd = request.POST.get('pwd', None)
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='management')
        cursor = conn.cursor()
        sql = 'select * from user where name = "'+ user+'" and password = "'+pwd+'"'
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
        except Exception as e:
            result = None
        finally:
            cursor.close()
            conn.close()
        if result:
            #去跳转到新页面
            return redirect('/data_page/')
        else:
            #用户名密码不匹配
            error_msg = '用户名或密码错误'
    return render(request,'user_login.html',{'error_msg':error_msg})

def userlist(request):

    if request.method == 'POST':
        username = request.POST.get('username',None)
        email = request.POST.get('email',None)
        gender = request.POST.get('gender',None)
        user_list.append({'username':username,'email':email,'gender':gender})
    return render(request, 'userlist.html', {'userlist': user_list})

def data_page(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='management', charset='utf8',cursorclass = pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    sql = 'select * from server_sys'
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as e:
        result = None
    finally:
        cursor.close()
        conn.close()
    return render(request, 'data_page.html',{'data':result})


def login(request):
    error_msg = ''
    if request.method == 'POST':
        #获取用户POST方法提交过来的数据
        print(request.POST)
        user = request.POST.get('username',None)
        pwd = request.POST.get('pwd',None)
        if user == 'root' and pwd == '123':
            #去跳转到新页面
            return redirect('http://www.baidu.com')
        else:
            #用户名密码不匹配
            error_msg = '用户名或密码错误'
    return render(request, 'login.html',{'error_msg':error_msg})

def day19(request):
    if request.method == 'POST':
        obj = request.POST
        print(obj)
        # v = obj.getlist('eat')
        # print(v)
        file = request.FILES.get('qqq')
        print(file,type(file))
        import os
        path = os.path.join('upload',file.name)
        f = open(path ,mode='wb')
        for item in file.chunks():
            f.write(item)
        f.close()

    return render(request,'day19.html')

def datail(request,**kw):
    print(kw)
    return HttpResponse(kw.values())

def states(request):
    # msg1 = ''
    # if request.method == 'POST':
    #     user = request.POST.get('user')
    #     pwd = request.POST.get('pwd')
    #     models.Userinfo.objects.create(username=user,password=pwd)
    #     msg1 = 'creat ok!'
    # return render(request,'adduser.html',{'msg':msg1})

    #查询
    # obj = models.Userinfo.objects.filter(username = 'root')[0]
    # print(obj)
    # print(obj.id ,obj.password)


    obj = models.Userinfo.objects.all()
    group = models.Group.objects.all()

    return render(request,'state.html',{'obj':obj})

def state(request,uid):
    obj = models.Userinfo.objects.filter(id = uid).first()
    return render(request, 'state_user.html', {'obj': obj})

def userdel(request,uid):
    models.Userinfo.objects.filter(id = uid).delete()
    return redirect('/cmdb/state')

def useredit(request,uid):
    if request.method == 'POST':
        un = request.POST.get('un',None)
        up = request.POST.get('up',None)
        em = request.POST.get('em',None)
        ug = request.POST.get('ug',1)
        if un and up:
            models.Userinfo.objects.filter(id = uid).update(username=un,password=up,email=em,usergroup_id = ug)
    obj = models.Userinfo.objects.filter(id=uid).first()
    group = models.Group.objects.all()
    return render(request, 'useredit.html', {'obj': obj,'group':group})

def group(request):

    msg = ''
    if request.method == 'POST':
        cf = request.POST.get('cf',None)
        cp = request.POST.get('cp',None)
        if cf and cp:
            models.Group.objects.create(classfiy = cf,caption = cp)
        else:
            msg = '组名和所属必须填写'
    obj = models.Group.objects.all()

    return render(request,'group.html',{'obj':obj,'msg':msg})

def groupdel(request,uid):
    models.Group.objects.filter(uid = uid).delete()
    return redirect('/cmdb/group')

def groupedit(request,uid):
    if request.method == 'POST':
        cla = request.POST.get('cla',None)
        cap = request.POST.get('cap',None)
        if cla and cap:
            models.Group.objects.filter(uid = uid).update(classfiy=cla,caption=cap)
    obj = models.Group.objects.filter(uid=uid).first()
    return render(request, 'groupedit.html', {'group': obj})

def adduser(request):
    msg = ''
    ht = 'adduser.html'
    if request.method == 'POST':
        name = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        mail = request.POST.get('email', None)
        group = request.POST.get('ug', 1)
        if name and pwd:
            models.Userinfo.objects.create(username=name, password=pwd, email=mail, usergroup_id=group)
            ht = 'state.html'
        else:
            msg = '用户名和密码必填'
    obj = models.Userinfo.objects.all()
    group = models.Group.objects.all()
    print(ht)
    return render(request,ht,{'obj':obj,'msg':msg,'group':group})


def addgroup(request):

    msg = ''
    ht = 'addgroup.html'
    if request.method == 'POST':
        cf = request.POST.get('cf',None)
        cp = request.POST.get('cp',None)
        if cf and cp:
            models.Group.objects.create(classfiy = cf,caption = cp)
            ht = 'group.html'
        else:
            msg = '组名和所属必须填写'
    obj = models.Group.objects.all()

    return render(request,ht,{'obj':obj,'msg':msg})

def groupminute(request,uid):
    obj = models.Group.objects.filter(uid = uid).first()
    ubj = models.Userinfo.objects.filter(usergroup_id = uid)
    return render(request, 'groupminute.html', {'obj': obj,'ubj':ubj})

def host(request):
    if request.method == 'POST':
        un = request.POST.get('un',None)
        up = request.POST.get('up',None)
        em = request.POST.get('em',None)
        ug = request.POST.get('ug',1)
        if un and up:
            models.Userinfo.objects.creat(username=un,password=up,email=em,usergroup_id = ug)
    obj = models.Userinfo.objects.all()
    gbj = models.Group.objects.all()
    return render(request, 'host.html', {'obj': obj,'gbj':gbj})

def test_ajax(request):
    print(request.method)
    username = request.GET.get('name')
    password = request.GET.get('pwd')
    email = request.GET.get('mail')
    usergroup_id = request.GET.get('g_id')
    print(request.GET)
    print(username,password,email,usergroup_id)
    return HttpResponse('我把门带上了')

def manyto(request):
#     obj = models.Userinfo.objects.get(id = 5)
#     obj.books.add(1,2)
#     obj = models.Userinfo.objects.get(id = 2)
#     obj.books.add(3)
#     obj = models.Userinfo.objects.get(id = 4)
#     obj.books.add(*[2,3,4])

    obj = models.Userinfo.objects.get(id = 4)
    print(obj.books.book_id)
    return HttpResponse('ok')

def test1(request):
    return render(request,'test1.html',{'name':"snnsNSNSnsnsSKKSss",'ss':'[1,2]'})


from utils import pagenation

def test2(request):
    curren_page = request.GET.get('p',1)
    curren_page = int(curren_page)

    li = []
    for i in range(45):
        li.append(i)
    obj = pagenation.Page(curren_page,len(li))
    data = li[obj.start():obj.end()]
    page_str = obj.page_str('/cmdb/test2_page/')

    return render(request, 'test2.html',{'data':data,'page_str':page_str})



# def test2(request):
#     li = []
#     sum_page = 7
#     page_num = 20
#     for i in range(495):
#         li.append(i)
#
#     current_page = request.GET.get("p",1)
#     current_page = int(current_page)
#     start = (current_page-1)*page_num
#     end = current_page*page_num
#
#     data = li[start:end]
#
#     all_count = len(li)
#     count , y = divmod(all_count,page_num)
#     if y>0:
#         count +=1
#     page_list=[]
#     if count < sum_page:
#         start_page = 1
#         end_page = count+1
#     else:
#         if current_page <=(sum_page+1)/2:
#             start_page = 1
#             end_page = sum_page+1
#         else:
#             start_page= current_page-(sum_page-1)/2
#             end_page = current_page + (sum_page + 1) / 2
#             if (count-current_page) < (sum_page+1)/2:
#                 start_page = count - sum_page
#                 end_page = count+1
#     prev = '<a class="page" href="?p=%s">上一页</a>'%(current_page-1)
#     if current_page == 1:
#         prev = '<a class="page" href="javascript:void(0)">上一页</a>'
#     page_list.append(prev)
#     for i in range(int(start_page),int(end_page)):
#         if i == current_page:
#             page = '<a class="page active" href="?p=%s">%s</a>'%(i,i)
#         else:
#             page = '<a class="page" href="?p=%s">%s</a>'%(i,i)
#
#         page_list.append(page)
#     next = '<a class="page" href="?p=%s">下一页</a>' % (current_page + 1)
#     if current_page == count:
#         next = '<a class="page" href="javascript:void(0)">下一页</a>'
#     page_list.append(next)
#     index = '''
#     <input type='text' id='i1'><input type='button' value='跳转' onclick='jumpTo(this,"/cmdb/test2_page/?p=");'>
#     <script>
#         function jumpTo(ths,base) {
#             var p = ths.previousSibling.value;
#             console.log(p,base);
#             location.href = base+p;
#
#         }
#     </script>'''
#     page_list.append(index)
#     page_str = ''.join(page_list)
#
#     return render(request,'test2.html',{"li":data,"page_str":page_str})