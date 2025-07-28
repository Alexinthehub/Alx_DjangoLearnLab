import os
import sys
import django

# 1. Set the Django settings module (Django looks here for config)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

# 2. Add base directory to sys.path so Python can import your app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 3. Setup Django
django.setup()

# 4. Now safely import your models
from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Queries ---

# Create Author
author = Author.objects.create(name="Ngugi wa Thiong’o", age=84)
print("✅ Author created:", author)

# Create Book and link to Author
book = Book.objects.create(title="Petals of Blood", publication_date="1977-01-01", author=author)
print("✅ Book created:", book)

# Create Library and add Book
library = Library.objects.create(name="Kenya National Library", location="Nairobi")
library.books.add(book)
print("✅ Library created and book added:", library)

# Create Librarian
librarian = Librarian.objects.create(name="Ann Mumbi", library=library)
print("✅ Librarian created:", librarian)
