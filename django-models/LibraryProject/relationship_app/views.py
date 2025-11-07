# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-Based View: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', { 'books': books })

# Class-Based View: show details for a specific library (including its books)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    # By default, detail view sends object as context_object_name, so in template you access `library`
    # You already have library.books because of the ManyToMany relation
