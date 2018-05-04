'''
Created on 2018年4月13日

@author: zhang
'''
from django import forms
from django.forms.widgets import Textarea

class ContactForm(forms.Form):
    subject = forms.CharField(max_length = 100)
    email = forms.EmailField(required = False,label='Your e-mail address')
    message = forms.CharField(widget = forms.Textarea)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.join(message.split()))
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
'''    
class Author_ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 40)
    age = forms.IntegerField()
    email = forms.EmailField(required = False)
    
class Blog_ContactForm(forms.Form):
    title = forms.CharField(max_length = 30)
    author = forms.ChoiceField(choices=Author)
    content =forms.CharField(max_length = 1000)
    blog_date = forms.DateField()
    website = forms.URLField(required = False)
'''
class Weibo_ContactForm(forms.Form):
    title = forms.CharField(max_length = 30)
    author = forms.CharField(max_length = 30)
    content =forms.CharField(widget = forms.Textarea)
    website = forms.URLField(required = False)
    weibo_date = forms.DateField(required = False)