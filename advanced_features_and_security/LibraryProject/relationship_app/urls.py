# In advanced_features_and_security/LibraryProject/relationship_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    list_books,
    LibraryDetailView,
    register,
    add_book,
    edit_book,
    delete_book  
)

urlpatterns = [
    # Existing paths from previous tasks
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Paths for custom permission views
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]