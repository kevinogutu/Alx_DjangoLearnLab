# relationship_app/urls.py
from .views import login_view, logout_view, register_view, list_books, LibraryDetailView
from django.urls import path
from .views import list_books        # ← make sure this line is present
from .views import LibraryDetailView  # also import if using the class-based view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]
