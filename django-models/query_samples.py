# query_samples.py
from relationship_app.models import Author, Book, Library, Librarian
from datetime import date

# Create an Author
author = Author.objects.create(name="Chinua Achebe", birth_date=date(1930, 11, 16))

# Create a Book linked to the Author
book = Book.objects.create(title="Things Fall Apart", publication_date=date(1958, 6, 17), author=author)

# Create a Library and add the Book
library = Library.objects.create(name="Central Library")
library.books.add(book)

# Create a Librarian assigned to the Library
librarian = Librarian.objects.create(name="Jane Doe", library=library)

# Sample Queries
# Retrieve all books by an author
author_books = Book.objects.filter(author=author)

# Retrieve all books in a library
library_books = library.books.all()

# Retrieve the librarian managing a library
library_librarian = Librarian.objects.get(library=library)

# Print some output
print("Author:", author.name)
print("Books by author:", [b.title for b in author_books])
print("Books in library:", [b.title for b in library_books])
print("Librarian:", library_librarian.name)
