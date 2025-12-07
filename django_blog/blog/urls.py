from django.urls import path
from .views import PostByTagListView
from .views import (
    # post_list_view,
    # post_detail_view,
    register_view,
    login_view,
    logout_view,
    profile_view,
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
    PostDeleteView,
)
from . import views as v  

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('post/<int:post_id>/', post_detail_view, name='post_detail'),

    # Authentication
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_id>/comments/<int:comment_pk>/edit/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('posts/<int:post_id>/comments/<int:comment_pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    # List & Detail (optional but recommended)
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('search/', views.search_posts, name='post_search'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),

]


