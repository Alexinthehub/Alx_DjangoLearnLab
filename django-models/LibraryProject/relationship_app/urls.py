from django.urls import path
from .views import list_books, LibraryDetailView # <-- This is the corrected import

urlpatterns = [
    # Use the imported functions directly
    path('books/', list_books, name='list_books'),
    path('library_detail/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]