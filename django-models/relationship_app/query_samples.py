# query_samples.py

import os
import sys
import django

# This line adds the parent directory to the Python path,
# allowing the script to find the LibraryProject module.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# The rest of your script remains the same
from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author (ForeignKey)
try:
    orwell = Author.objects.get(name='George Orwell')
    orwell_books = Book.objects.filter(author=orwell)
    print("Books by George Orwell:")
    for book in orwell_books:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print("Author 'George Orwell' not found.")

print("\n" + "="*20 + "\n")

# Query 2: All books in a library (ManyToMany)
try:
    city_library = Library.objects.get(name='City Library')
    library_books = city_library.books.all()
    print("Books in City Library:")
    for book in library_books:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print("Library 'City Library' not found.")

print("\n" + "="*20 + "\n")

# Query 3: Retrieve the librarian for a library (OneToOne)
try:
    city_library = Library.objects.get(name='City Library')
    librarian_name = city_library.librarian.name
    print(f"Librarian for City Library is: {librarian_name}")
except Library.DoesNotExist:
    print("Library 'City Library' not found.")
except Librarian.DoesNotExist:
    print("Librarian not found for City Library.")