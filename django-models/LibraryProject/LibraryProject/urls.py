from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # The 'bookshelf' app is where we are working
    path('', include('bookshelf.urls')), 
    # Remove the problematic include for the relationship_app
    # path('', include('LibraryProject.relationship_app.urls')),
]