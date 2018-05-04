from django.contrib import admin
from weibo.models import Weibo

# Register your models here.


class WeiboAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','author','weibo_date')
    list_filter = ('weibo_date',)
admin.site.register(Weibo,WeiboAdmin)