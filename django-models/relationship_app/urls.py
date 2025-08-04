# In django-models/relationship_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views  # Add this import
from .views import list_books, LibraryDetailView, register  # Add 'register' to this import

urlpatterns = [
    # Paths from previous task
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Paths for current task
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]