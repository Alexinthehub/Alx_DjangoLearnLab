# In django-models/relationship_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    list_books,
    LibraryDetailView,
    register,
    admin_view,     # Add this
    librarian_view, # Add this
    member_view,    # Add this
)

urlpatterns = [
    # Existing paths from previous tasks
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Paths for current task
    path('admin-dashboard/', admin_view, name='admin_dashboard'),
    path('librarian-panel/', librarian_view, name='librarian_panel'),
    path('member-dashboard/', member_view, name='member_dashboard'),
]