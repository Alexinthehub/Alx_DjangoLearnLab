# bookshelf/admin.py

from django.contrib import admin
from .models import Book

# Create a custom Admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# Register the Book model with the custom Admin class
admin.site.register(Book, BookAdmin)