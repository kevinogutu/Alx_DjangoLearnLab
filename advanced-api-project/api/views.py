from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# ---
# Step 1: Set Up Generic Views (Separated)
# ---

# 1. ListView (Read-Only)
class BookListView(generics.ListAPIView):
    """
    Handles: GET /api/v1/books/
    - Retrieves a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Read-only, so IsAuthenticatedOrReadOnly allows all GET requests
    permission_classes = [IsAuthenticatedOrReadOnly]


# 2. DetailView (Read-Only)
class BookDetailView(generics.RetrieveAPIView):
    """
    Handles: GET /api/v1/books/<int:pk>/
    - Retrieves a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# 3. CreateView (Write-Only)
class BookCreateView(generics.CreateAPIView):
    """
    Handles: POST /api/v1/books/create/
    - Creates a new book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Write-only, so IsAuthenticatedOrReadOnly requires authentication
    permission_classes = [IsAuthenticatedOrReadOnly] # Effectively IsAuthenticated
    
    # Step 3: Customization
    def perform_create(self, serializer):
        """Custom hook for creation."""
        serializer.save()
        print(f"New book created: {serializer.instance.title}")


# 4. UpdateView (Write-Only)
class BookUpdateView(generics.UpdateAPIView):
    """
    Handles: PUT /api/v1/books/<int:pk>/update/
    - Modifies an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Effectively IsAuthenticated


# 5. DeleteView (Write-Only)
class BookDeleteView(generics.DestroyAPIView):
    """
    Handles: DELETE /api/v1/books/<int:pk>/delete/
    - Removes an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Effectively IsAuthenticated