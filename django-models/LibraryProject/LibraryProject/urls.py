# File: LibraryProject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookshelf.urls')),  # Include the URLs from your bookshelf app
]