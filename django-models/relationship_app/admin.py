from django.contrib import admin
<<<<<<< HEAD
from .models import Author, Book, Library, Librarian

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author")
    list_filter = ("author",)
    search_fields = ("title", "author__name")

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    filter_horizontal = ("books",)

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "library")
    search_fields = ("name", "library__name")
=======

# Register your models here.
>>>>>>> aea86264ebf01363a67a1d20dbc3f7bce3c4d97b
