from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookshelf.urls')),  # Include the urls from the bookshelf app
    path('accounts/', include('django.contrib.auth.urls')), # To handle login/logout
]