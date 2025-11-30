from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter  


class BookListView(generics.ListAPIView):
    """
    Handles: GET /api/v1/books/
    
    Provides a list of all books with advanced query capabilities:
    - Filtering (by title, author, publication_year, isbn)
    - Searching (on title and author fields)
    - Ordering (by title, published_date)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Step 1, 2, 3: Configure Backends
    filter_backends = [
        DjangoFilterBackend,  # Step 1: Filtering
        SearchFilter,         # Step 2: Searching
        OrderingFilter        # Step 3: Ordering
    ]
    
  
  
    filterset_class = BookFilter

    
    search_fields = ['title', 'author']

   
    ordering_fields = ['title', 'published_date']
    
    
    ordering = ['published_date']



class BookDetailView(generics.RetrieveAPIView):
    """ Handles: GET /api/v1/books/<int:pk>/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class BookCreateView(generics.CreateAPIView):
    """ Handles: POST /api/v1/books/create/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save()



class BookUpdateView(generics.UpdateAPIView):
    """ Handles: PUT /api/v1/books/update/<int:pk>/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]



class BookDeleteView(generics.DestroyAPIView):
    """ Handles: DELETE /api/v1/books/delete/<int:pk>/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]