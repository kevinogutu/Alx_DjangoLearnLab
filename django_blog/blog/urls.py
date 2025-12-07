from django.urls import path
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
