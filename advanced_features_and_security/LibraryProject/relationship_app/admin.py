# In LibraryProject/relationship_app/admin.py
from django.contrib import admin
from .models import Book, Author, Library

# We removed the CustomUser model from this app,
# so we also remove its admin registration.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)