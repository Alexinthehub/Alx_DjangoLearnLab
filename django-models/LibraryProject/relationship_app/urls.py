from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.list_books, name='home'),
    path('books/', views.list_books, name='list_books'),
    path('library_detail/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # New URL patterns for authentication
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html', next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
]