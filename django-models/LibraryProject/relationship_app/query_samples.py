# In relationship_app/query_samples.py
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Queries ---

# Query all books by a specific author (ForeignKey)
def query_books_by_author(author_name):
    print(f"\n--- Books by {author_name} (ForeignKey) ---")
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        if books:
            for book in books:
                print(f"Title: {book.title}")
        else:
            print(f"No books found for {author_name}.")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")

# List all books in a library (ManyToMany)
def query_books_in_library(library_name):
    print(f"\n--- Books in {library_name} (ManyToMany) ---")
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        if books:
            for book in books:
                print(f"Title: {book.title} by {book.author.name}")
        else:
            print(f"No books found in {library_name}.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

# Retrieve the librarian for a library (OneToOne)
def query_librarian_for_library(library_name):
    print(f"\n--- Librarian for {library_name} (OneToOne) ---")
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")

if __name__ == '__main__':
    print("Running sample queries...")

    # Create some sample data for testing
    print("\nCreating sample data...")
    author1, _ = Author.objects.get_or_create(name='J.R.R. Tolkien')
    author2, _ = Author.objects.get_or_create(name='J.K. Rowling')

    book1, _ = Book.objects.get_or_create(title='The Hobbit', author=author1)
    book2, _ = Book.objects.get_or_create(title='The Fellowship of the Ring', author=author1)
    book3, _ = Book.objects.get_or_create(title='Harry Potter and the Sorcerer\'s Stone', author=author2)

    library1, _ = Library.objects.get_or_create(name='Central Library')
    library1.books.add(book1, book3)
    library2, _ = Library.objects.get_or_create(name='Riverside Library')
    library2.books.add(book2)

    librarian1, _ = Librarian.objects.get_or_create(name='Sarah Connor', library=library1)
    librarian2, _ = Librarian.objects.get_or_create(name='John Smith', library=library2)
    print("Sample data created.")

    # Run the queries
    query_books_by_author('J.R.R. Tolkien')
    query_books_in_library('Central Library')
    query_librarian_for_library('Riverside Library')