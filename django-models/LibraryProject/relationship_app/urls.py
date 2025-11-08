# relationship_app/urls.py
from .views import login_view, logout_view, register_view, list_books, LibraryDetailView
from django.urls import path
from .views import list_books        # ← make sure this line is present
from .views import LibraryDetailView  # also import if using the class-based view
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    # … other URL patterns for your app …
]
# relationship_app/urls.py



urlpatterns = [
    path('admin-page/', admin_view, name='admin_view'),
    path('librarian-page/', librarian_view, name='librarian_view'),
    path('member-page/', member_view, name='member_view'),
]


urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),       # <-- add_book/ path
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),  # <-- edit_book/ path
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
    # ... other URL patterns ...
]
