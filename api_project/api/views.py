# In api_project/api/views.py

from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# This is the old view, keep it for now as per task description
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for all CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer