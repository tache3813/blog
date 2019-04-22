from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category, Comment, Description

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Description)
