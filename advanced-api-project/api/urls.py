from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    # Endpoint for listing all books and creating a new one
    path('books/', BookListCreateView.as_view(), name='book-list-create'),

    # Endpoint for retrieving, updating, or deleting a specific book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]