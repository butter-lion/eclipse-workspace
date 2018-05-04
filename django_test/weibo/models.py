from django.db import models

# Create your models here.
class Weibo(models.Model):
    title = models.CharField(max_length = 30)
    content =models.TextField(max_length = 1000)
    author = models.CharField(max_length = 30)
    website = models.URLField(blank = True)
    weibo_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.title
    class META:
        ordering = ['title']
    