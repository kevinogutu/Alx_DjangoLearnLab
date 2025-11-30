from django.urls import path
from . import views

urlpatterns = [
    # Read-Only Endpoints
    # GET /api/v1/books/
    path('books/', views.BookListView.as_view(), name='book-list'),
    
    # GET /api/v1/books/<int:pk>/
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    
    # Write-Only Endpoints
    
    # POST /api/v1/books/create/
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    
    # PUT/PATCH /api/v1/books/update/<int:pk>/
    path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),
    
    # DELETE /api/v1/books/delete/<int:pk>/
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),
]