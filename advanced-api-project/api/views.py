from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# This view handles listing all books and creating a new book.
# Read-only for all users; authenticated users can create.
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# This view handles retrieving, updating, and deleting a single book.
# All actions require authentication.
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]