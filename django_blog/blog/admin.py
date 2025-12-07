from django.urls import path
from django.contrib import admin
from .models import Post, Comment
from taggit.admin import TaggableManager

from .views import (
    post_list_view,
    post_detail_view,
    register_view,
    login_view,
    logout_view,
    profile_view,
)

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('post/<int:post_id>/', post_detail_view, name='post_detail'),

    # Authentication
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'content', 'tags__name')
    list_filter = ('published_date', 'author')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at', 'updated_at')
    search_fields = ('content', 'author__username', 'post__title')
    list_filter = ('created_at', 'author')


