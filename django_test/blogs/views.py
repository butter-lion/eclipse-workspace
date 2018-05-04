from django.shortcuts import render
from blogs.models import Blog

# Create your views here.

def blogs_list(request):
    lists = Blog.objects.all()
    return render(request, 'blog_list.html',{'lists':lists})

'''
def blog_text(request):
    
    return render(request, 'blog_text.html')

def blog_add(request):
    return render(request, 'blog_add.html')

def blog_change(request):
    return render(request,'blog_change.html')

def blog_author(request):
    return render(request, 'blog_author.html')

def blog_author_add(request):
    return render(request, 'blog_author_add.html')

def blog_auther_change(request):
    return render(request,'blog_author_change.html')
'''
'''
def contact(request):
    if request.method == 'POST':
        form = Author_ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                '540658957@qq.com',
                [cd['email']],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = Author_ContactForm()
    return render(request, 'contact_form.html',{'form':form})
'''