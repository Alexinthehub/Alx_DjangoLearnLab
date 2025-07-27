# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# Create Authors
author1 = Author.objects.create(name="Chinua Achebe")
author2 = Author.objects.create(name="Ngugi wa Thiong'o")

# Create Books and link authors
book1 = Book.objects.create(title="Things Fall Apart")
book1.authors.add(author1)

book2 = Book.objects.create(title="The River Between")
book2.authors.add(author2)

# Create Library and add books
library = Library.objects.create(name="East African Library")
library.books.set([book1, book2])

# Create a Librarian for the library
librarian = Librarian.objects.create(name="Mr. Otieno", library=library)

# Sample queries
print("Books in the library:")
for book in library.books.all():
    print(f" - {book.title}")

print("\nAuthors of 'Things Fall Apart':")
for author in book1.authors.all():
    print(f" - {author.name}")

print(f"\nLibrarian at {library.name}: {librarian.name}")

