from django.urls import path
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
      # List and detail views
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),

    # Create, update, delete — CRUD operations
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]



from django.urls import path
from . import views


