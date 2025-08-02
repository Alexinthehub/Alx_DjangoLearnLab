from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('roles/', include('bookshelf.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # includes login
]
