from django.contrib import admin
from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title','text','create_date','published_date')
    list_filter  = ('author','create_date','published_date')
    list_per_page= 15
    search_fields =('author','title','create_date','published_date')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('post','author','text','create_date','approved_comment')
    list_filter  = ('author' ,'create_date','approved_comment')
    list_per_page = 15
    search_fields = ('author' ,'create_date','approved_comment')


admin.site.register(Post ,PostAdmin)
admin.site.register(Comments ,CommentsAdmin)
