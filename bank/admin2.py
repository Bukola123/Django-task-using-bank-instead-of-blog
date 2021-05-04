from django.contrib import admin
from .models import Post, Comment



admin.site.register(Post, Admin)
admin.site.register(Comment)


class CommentInLine(admin.StackedInLine):
    model  = Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]





