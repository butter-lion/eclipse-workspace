'''
Created on 2018年4月12日

@author: zhang
'''
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from contact.forms import ContactForm
from django.core.mail import send_mail

def contact_thanks(request):
    return HttpResponse('welcome to join us')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
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
        form = ContactForm()
    return render(request, 'contact_form.html',{'form':form})

