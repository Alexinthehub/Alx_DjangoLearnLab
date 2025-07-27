import os
import sys
import django

# ✅ Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ✅ Point to the settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

django.setup()

# 👇 Now you can safely import models
from relationship_app.models import Author, Book, Library, Librarian


# ✅ Create or get an author
author, created = Author.objects.get_or_create(name="Chinua Achebe")
print(f"Author: {author.name} (Created: {created})")

# ✅ Create or get a book for the author
book, created = Book.objects.get_or_create(
    title="Things Fall Apart",
    defaults={'author': author}
)
if not created:
    book.author = author  # ensure the author is correct
    book.save()
print(f"Book: {book.title} (Created: {created})")

# ✅ Create or get a library
library, created = Library.objects.get_or_create(name="Central Library")
print(f"Library: {library.name} (Created: {created})")

# ✅ Add the book to the library (many-to-many)
library.books.add(book)
print(f"Book '{book.title}' added to library '{library.name}'")

# ✅ Create or get a librarian for the library
librarian, created = Librarian.objects.get_or_create(
    name="Jane Doe",
    defaults={'library': library}
)
if not created:
    librarian.library = library  # ensure correct link
    librarian.save()
print(f"Librarian: {librarian.name} (Created: {created})")
