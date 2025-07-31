from relationship_app.models import Author, Book, Library, Librarian

# Create an author
author = Author.objects.create(name="Chinua Achebe", age=45)

# Create a book
book = Book.objects.create(title="Things Fall Apart", author=author)

# Create a library
library = Library.objects.create(name="Central Library")
library.books.add(book)

# Create a librarian
librarian = Librarian.objects.create(name="Mr. Otieno", library=library)
