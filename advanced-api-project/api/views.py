# api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly  # allows read for all, write for authenticated
from .models import Book
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    GET: list all books
    POST: create a new book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allow anyone to view, but require authentication for create
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Optional: override perform_create if you need custom logic on save
    # def perform_create(self, serializer):
    #     serializer.save()

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: retrieve a book by ID
    PUT/PATCH: update an existing book
    DELETE: remove a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # lookup_field defaults to 'pk', so /books/<int:pk>/ works
