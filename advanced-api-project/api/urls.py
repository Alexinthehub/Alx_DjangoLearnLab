from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # Endpoint for listing all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Endpoint for creating a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Endpoint for a single book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Endpoint for updating a book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # Endpoint for deleting a book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]