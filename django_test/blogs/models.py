from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    age = models.IntegerField()
    email = models.EmailField('e-mail',blank = True)
    def __str__(self):
        return u'%s %s' %(self.first_name,self.last_name)
    class META:
        ordering = ['first_name']
        
class Blog(models.Model):
    title = models.CharField(max_length = 30)
    content =models.TextField(max_length = 1000)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    website = models.URLField(blank = True)
    blog_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.title
    class META:
        ordering = ['title']