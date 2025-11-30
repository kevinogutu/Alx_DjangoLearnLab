from rest_framework import generics
# Step 4: Import the required permission classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# ---
# Step 1: Set Up Generic Views
# ---

# 1. ListView (Read-Only)
class BookListView(generics.ListAPIView):
    """ Handles: GET /api/v1/books/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Step 4: Allow read-only access to anyone
    permission_classes = [IsAuthenticatedOrReadOnly]


# 2. DetailView (Read-Only)
class BookDetailView(generics.RetrieveAPIView):
    """ Handles: GET /api/v1/books/<int:pk>/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Step 4: Allow read-only access to anyone
    permission_classes = [IsAuthenticatedOrReadOnly]


# 3. CreateView (Write-Only)
class BookCreateView(generics.CreateAPIView):
    """ Handles: POST /api/v1/books/create/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Step 4: Require authentication for creating
    permission_classes = [IsAuthenticated]
    
    # Step 3: Customization
    def perform_create(self, serializer):
        serializer.save()


# 4. UpdateView (Write-Only)
class BookUpdateView(generics.UpdateAPIView):
    """ Handles: PUT /api/v1/books/update/<int:pk>/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Step 4: Require authentication for updating
    permission_classes = [IsAuthenticated]


# 5. DeleteView (Write-Only)
class BookDeleteView(generics.DestroyAPIView):
    """ Handles: DELETE /api/v1/books/delete/<int:pk>/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Step 4: Require authentication for deleting
    permission_classes = [IsAuthenticated]