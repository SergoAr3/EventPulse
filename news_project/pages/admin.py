from django.contrib import admin
from models import Article, Comment, Event


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'image']


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Event)
