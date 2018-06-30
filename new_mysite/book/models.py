from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)
    email = models.EmailField('e-mail')
    phone = models.IntegerField(blank=True,null=True)
    register_time = models.DateTimeField(auto_now_add=True)

class Publisher(models.Model):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    website = models.URLField(max_length=200)

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField('e-mail', blank=True)

class Book(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField(to = 'Author',related_name='books')
    publisher = models.ForeignKey('Publisher',on_delete=models.CASCADE,related_name='books')
    publication_date = models.DateField(blank=True, null=True)
