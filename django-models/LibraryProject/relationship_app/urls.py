# relationship_app/urls.py

from django.urls import path
from .views import list_books        # ← make sure this line is present
from .views import LibraryDetailView  # also import if using the class-based view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
