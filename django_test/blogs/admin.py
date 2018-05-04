from django.contrib import admin

# Register your models here.
from blogs.models import Blog, Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age','email')
    search_fields = ('first_name','last_name')
   
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','author','blog_date')
    list_filter = ('blog_date',)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Author,AuthorAdmin)