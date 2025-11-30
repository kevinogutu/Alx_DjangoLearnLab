from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# 1. ListView (Read-Only)
class BookListView(generics.ListAPIView):
    """ Handles: GET /api/v1/books/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# 2. DetailView (Read-Only)
class BookDetailView(generics.RetrieveAPIView):
    """ Handles: GET /api/v1/books/<int:pk>/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# 3. CreateView (Write-Only)
class BookCreateView(generics.CreateAPIView):
    """ Handles: POST /api/v1/books/create/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Effectively IsAuthenticated
    
    def perform_create(self, serializer):
        serializer.save()


# 4. UpdateView (Write-Only)
class BookUpdateView(generics.UpdateAPIView):
    """ Handles: PUT /api/v1/books/update/<int:pk>/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Effectively IsAuthenticated


# 5. DeleteView (Write-Only)
class BookDeleteView(generics.DestroyAPIView):
    """ Handles: DELETE /api/v1/books/delete/<int:pk>/ """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Effectively IsAuthenticated