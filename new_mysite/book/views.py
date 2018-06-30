from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect,render,HttpResponse
from book import models
from utils import pagenation
from django import views


def cookie(func):
    def inner(request,*args,**kwargs):
        v = request.COOKIES.get('user')
        if not v:
            res = redirect('/book/login/')
            return res
        return func(request,*args,**kwargs)
    return inner

def login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        d = models.User.objects.filter(username =u,pwd=p).first()
        if d:
            res = redirect('/book/books/')
            res.set_cookie('user', u, path='/book/')
            return res
    cook = '未登录'
    return render(request, 'book/login.html',{'username':cook})

class register(views.View):

    def get(self,request):
        cook = '未登录'
        return render(request, 'book/register.html', {'username': cook})

    def post(self,request):
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        e = request.POST.get('email')
        ph = request.POST.get('phone')
        if u and p and e and ph:
            models.User.objects.create(username=u,pwd=p,email=e,phone=int(ph))
            return redirect('/book/register_ok/')
        return redirect('/book/register/')

def register_ok(request):
    cook = '未登录'
    return render(request, 'book/register_ok.html', {'username': cook})

@cookie
def books(request):
    cook = request.COOKIES.get('user')
    curren_page = request.GET.get('p', 1)
    curren_page = int(curren_page)
    books_list = models.Book.objects.all()
    len_books = books_list.count()
    obj = pagenation.Page(curren_page, len_books)
    data = books_list[obj.start():obj.end()]
    page_str = obj.page_str('/book/books/')
    return render(request,'book/books.html',{'books_list':data,'page_str':page_str,'username':cook})

@cookie
def authors(request):
    cook = request.COOKIES.get('user')
    curren_page = request.GET.get('p', 1)
    curren_page = int(curren_page)
    authors_list = models.Author.objects.all()
    len_authors = authors_list.count()
    obj = pagenation.Page(curren_page, len_authors)
    data = authors_list[obj.start():obj.end()]
    page_str = obj.page_str('/book/authors/')
    return render(request,'book/authors.html',{'authors_list':data,'page_str':page_str,'username':cook})

@cookie
def publishers(request):
    cook = request.COOKIES.get('user')
    curren_page = request.GET.get('p', 1)
    curren_page = int(curren_page)
    publishers_list = models.Publisher.objects.all()
    len_publishers = publishers_list.count()
    obj = pagenation.Page(curren_page, len_publishers)
    data = publishers_list[obj.start():obj.end()]
    page_str = obj.page_str('/book/publishers/')
    return render(request, 'book/publishers.html', {'publishers_list': data, 'page_str': page_str,'username':cook})

@cookie
def books_add(request):
    if request.method == 'POST':
        t = request.POST.get('book_title')
        a= request.POST.getlist('authors')
        p= request.POST.get('publisher')
        b_t = request.POST.get('book_time')
        if t and a and p:
            obj = models.Book.objects.create(title=t,publisher_id=p,publication_date = b_t)
            obj.authors.add(*a)
            return redirect('/book/books/')
    cook = request.COOKIES.get('user')
    authors_list = models.Author.objects.all()
    publishers_list = models.Publisher.objects.all()
    return render(request,'book/books_add.html',{'authors_list':authors_list,'publishers_list':publishers_list,'username':cook})

@cookie
def books_del(request,did):
    models.Book.objects.filter(id=did).delete()
    return redirect('/book/books')

@cookie
def books_set(request,sid):
    if request.method == 'POST':
        t = request.POST.get('book_title')
        a= request.POST.getlist('authors')
        p= request.POST.get('publisher')
        b_t = request.POST.get('book_time')
        if t and a and p:
            models.Book.objects.filter(id=sid).update(title=t,publisher_id=p,publication_date = b_t)
            obj = models.Book.objects.filter(id=sid).first()
            print(a)
            obj.authors.set(a)
            return redirect('/book/books/')
    cook = request.COOKIES.get('user')
    authors_list = models.Author.objects.all()
    publishers_list = models.Publisher.objects.all()
    book_obj = models.Book.objects.filter(id = sid).first()
    book_date = str(book_obj.publication_date)
    au_list = []
    auth_list = book_obj.authors.all()
    for a in auth_list:
        au_list.append(a.id)
    print(au_list)
    return render(request,'book/books_set.html',{'authors_list':authors_list,'publishers_list':publishers_list,'book_obj':book_obj,'book_date':book_date,'au_list':au_list,'username':cook})

@cookie
def authors_add(request):
    if request.method == 'POST':
        fn = request.POST.get('author_fn')
        ln= request.POST.get('author_ln')
        email= request.POST.get('author_email')
        if fn and ln and email:
            models.Author.objects.create(first_name=fn,last_name=ln,email=email)
            return redirect('/book/authors/')
    cook = request.COOKIES.get('user')
    return render(request,'book/authors_add.html',{'username':cook})

@cookie
def authors_del(request,did):
    models.Author.objects.filter(id=did).delete()
    return redirect('/book/authors')

@cookie
def authors_set(request,sid):
    if request.method == 'POST':
        fn = request.POST.get('author_fn')
        ln= request.POST.get('author_ln')
        email= request.POST.get('author_email')
        if fn and ln and email:
            models.Author.objects.filter(id=sid).update(first_name=fn,last_name=ln,email=email)
            return redirect('/book/authors/')
    cook = request.COOKIES.get('user')
    au_obj = models.Author.objects.filter(id=sid).first()
    return render(request,'book/authors_set.html',{'au_obj':au_obj,'username':cook})

@cookie
def publishers_add(request):
    if request.method == 'POST':
        pub_name = request.POST.get('pub_name')
        pub_country= request.POST.get('pub_country')
        pub_city= request.POST.get('pub_city')
        pub_address= request.POST.get('pub_address')
        pub_website= request.POST.get('pub_website')
        if pub_name and pub_country and pub_city and pub_address:
            models.Publisher.objects.create(name=pub_name,country=pub_country,city=pub_city,address = pub_address,website=pub_website)
            return redirect('/book/publishers/')
    cook = request.COOKIES.get('user')
    return render(request,'book/publishers_add.html',{'username':cook})

@cookie
def publishers_del(request,did):
    models.Publisher.objects.filter(id=did).delete()
    return redirect('/book/publishers')

@cookie
def publishers_set(request,sid):
    if request.method == 'POST':
        pub_name = request.POST.get('pub_name')
        pub_country= request.POST.get('pub_country')
        pub_city= request.POST.get('pub_city')
        pub_address= request.POST.get('pub_address')
        pub_website= request.POST.get('pub_website')
        if pub_name and pub_country and pub_city and pub_address:
            models.Publisher.objects.filter(id=sid).update(name=pub_name,country=pub_country,city=pub_city,address = pub_address,website=pub_website)
            return redirect('/book/publishers/')
    cook = request.COOKIES.get('user')
    pub_obj = models.Publisher.objects.filter(id=sid).first()
    return render(request,'book/publishers_set.html',{'pub_obj':pub_obj,'username':cook})