from django.contrib import admin

# Register your models here.

from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__", "data", "tag"]
    list_filter = ["data"]
    search_fields = ["titolo", "contenuto", "tag"]
    prepopulated_fields = {"slug": ("titolo",)}

    class Meta:
        model = Post

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Post, PostAdmin) 