# In LibraryProject/bookshelf/urls.py

from django.urls import path
from . import views
app_name = 'bookshelf' 

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
]