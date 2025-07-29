import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# ✅ Create sample authors
author1 = Author.objects.create(name="Chinua Achebe", birthdate="1930-01-01")
author2 = Author.objects.create(name="Ngũgĩ wa Thiong'o", birthdate="1938-01-05")

# ✅ Create sample books
book1 = Book.objects.create(title="Things Fall Apart", publication_year=1958, author=author1)
book2 = Book.objects.create(title="The River Between", publication_year=1965, author=author2)

# ✅ Create a library and add books to it
library = Library.objects.create(name="National Library")
library.books.set([book1, book2])  # Many-to-Many relationship

# ✅ Assign a librarian to the library
librarian = Librarian.objects.create(name="Jane Doe", library=library)

# ✅ Print all books with their authors
print("\nBooks and their authors:")
for book in Book.objects.all():
    print(f"{book.title} ({book.publication_year}) by {book.author.name}")

# ✅ Print all libraries and their books
print("\nLibraries and their books:")
for lib in Library.objects.all():
    print(f"Library: {lib.name}")
    for book in lib.books.all():
        print(f" - {book.title} by {book.author.name}")

# ✅ Print librarian and their library
print("\nLibrarians and their libraries:")
for librarian in Librarian.objects.all():
    print(f"{librarian.name} works at {librarian.library.name}")
