# query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# Sample Query 1: Create an Author
author = Author.objects.create(name="Ngũgĩ wa Thiong'o")

# Sample Query 2: Create a Book and assign the author
book = Book.objects.create(title="The River Between", author=author)

# Sample Query 3: Create a Library and add the book
library = Library.objects.create(name="Kenya National Library")
library.books.add(book)

# Sample Query 4: Create a Librarian assigned to the Library
librarian = Librarian.objects.create(name="Jane Doe", library=library)

# Retrieve all books in the library
books_in_library = library.books.all()
print("Books in library:", books_in_library)
