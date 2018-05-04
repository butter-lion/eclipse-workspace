from django.shortcuts import render
from weibo.models import Weibo
from contact.forms import Weibo_ContactForm

# Create your views here.
def weibos_list(request):
    lists = Weibo.objects.all()
    return render(request, 'weibos_list.html',{'lists':lists})

def weibo_page(request, weibo_id):
    weibo = Weibo.objects.get(pk = weibo_id)
    return render(request , 'weibo_page.html',{'weibo':weibo})
'''
def weibo_contact(request):
    
    if request.method == 'POST':
        form = Weibo_ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Weibo.objects.create(title=cd['title'],content=cd['content'],author=cd['author'],website=cd['website'],weibo_date=cd['weibo_date'])
            lists = Weibo.objects.all()
            return render(request, 'weibos_list.html',{'lists':lists})
    else:
        form = Weibo_ContactForm()
        return  render(request, 'weibo_form.html',{'form':form})
'''
def weibo_remake(request,weibo_id):

    if request.method == 'POST':
        form = Weibo_ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if weibo_id == 0:
                Weibo.objects.create(title =cd['title'],content=cd['content'],author=cd['author'],website=cd['website'],weibo_date=cd['weibo_date'])
            else:
                w = Weibo.objects.get(pk = weibo_id)
                w.title =cd['title']
                w.content=cd['content']
                w.author=cd['author']
                w.website=cd['website']
                w.weibo_date=cd['weibo_date']
                w.save()
            lists = Weibo.objects.all()
            return render(request, 'weibos_list.html',{'lists':lists})
        
    else:
        if weibo_id == 0:
            form = Weibo_ContactForm()
            return  render(request, 'weibo_form.html',{'form':form})
        else:   
            weibo = Weibo.objects.get(pk = weibo_id)
            form = Weibo_ContactForm(
                      initial={'title':weibo.title,
                               'content':weibo.content,
                               'author':weibo.author,
                               'website':weibo.website,
                               'weibo_date':weibo.weibo_date}
                      )
            return  render(request, 'weibo_form.html',{'form':form})
        