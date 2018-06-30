from django.shortcuts import render,redirect

# Create your views here.

dict={'dachengzi':123123,
      ' ':321321}

def login(request):
    if request.method == 'GET':
        return render(request,'mainpage/login.html')
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        v = dict.get(u)
        print(v)
        if not v:
            return render(request, 'mainpage/login.html')
        if str(v) == p:
            res = redirect('/mainpage/index/')
            res.set_cookie('user',u)
            return res


def index(request):
    user1 = request.COOKIES.get('user')
    if user1:
        return render(request,'mainpage/index.html',{'username':user1})
    else:
        return render(request,'mainpage/login.html')