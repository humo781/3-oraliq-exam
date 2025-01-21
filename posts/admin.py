from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'image', 'catalog', 'created_at')
    search_fields = ('title',)
    list_filter = ('title', 'created_at')
    ordering = ('created_at',)
    exclude = ('slug',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('post', 'author')
    list_filter = ('author', 'post')
    ordering = ('post', 'author')
