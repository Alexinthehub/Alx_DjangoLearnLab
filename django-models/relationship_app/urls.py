# relationship_app/urls.py

# relationship_app/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', views.book_list_view, name='book-list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-dashboard/', views.admin_view, name='admin-dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian-dashboard'),
    path('member-dashboard/', views.member_view, name='member-dashboard'),
]