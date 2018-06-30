from django.db import models

# Create your models here.
class Group(models.Model):
    uid = models.IntegerField(auto_created=True ,primary_key=True)
    classfiy = models.CharField(max_length=32,unique=True)
    caption = models.CharField(max_length=32,null=True)
    ctime = models.DateTimeField(auto_now=True,null=True)

class Userinfo(models.Model):

    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=64,null=True)
    creattime = models.DateTimeField(auto_now=True,null=True)
    usergroup = models.ForeignKey('Group',default=1, on_delete=models.CASCADE)
    books = models.ManyToManyField('Book')


class Book(models.Model):
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=32)

