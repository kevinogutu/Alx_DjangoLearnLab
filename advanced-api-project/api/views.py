from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# Step 2 & 3: Import the 'filters' module from rest_framework
from rest_framework import filters 
# Step 1: Import 'rest_framework' from 'django_filters'
from django_filters import rest_framework 
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter

# ---
# 1. ListView (With corrected backend references)
# ---
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
    
    # Step 1, 2, 3: Configure Backends using the module imports
    filter_backends = [
        rest_framework.DjangoFilterBackend,  # From django_filters
        filters.SearchFilter,                # From rest_framework
        filters.OrderingFilter               # From rest_framework
    ]
    
    # --- Step 1: Filtering Configuration ---
    filterset_class = BookFilter

    # --- Step 2: Search Configuration ---
    search_fields = ['title', 'author']

    # --- Step 3: Ordering Configuration ---
    ordering_fields = ['title', 'published_date']
    ordering = ['published_date']


# ---
# 2. DetailView (No changes)
# ---
class BookDetailView(generics.RetrieveAPIView):
    """ Handles: GET /api/v1/books/<int:pk>/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ---
# 3. CreateView (No changes)
# ---
class BookCreateView(generics.CreateAPIView):
    """ Handles: POST /api/v1/books/create/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save()


# ---
# 4. UpdateView (No changes)
# ---
class BookUpdateView(generics.UpdateAPIView):
    """ Handles: PUT /api/v1/books/update/<int:pk>/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ---
# 5. DeleteView (No changes)
# ---
class BookDeleteView(generics.DestroyAPIView):
    """ Handles: DELETE /api/v1/books/delete/<int:pk>/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]