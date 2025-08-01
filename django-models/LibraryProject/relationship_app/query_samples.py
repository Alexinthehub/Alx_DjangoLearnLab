from LibraryProject.relationship_app.models import Author, Book, Library, Librarian

# Clean up any existing data to ensure a fresh run
Author.objects.all().delete()
Book.objects.all().delete()
Library.objects.all().delete()
Librarian.objects.all().delete()

# --- Sample Data Creation ---

author1 = Author.objects.create(name="Chinua Achebe")
author2 = Author.objects.create(name="Ngugi wa Thiong'o")

book1 = Book.objects.create(title="Things Fall Apart", author=author1)
book2 = Book.objects.create(title="The River Between", author=author2)
book3 = Book.objects.create(title="Weep Not, Child", author=author2)

library1 = Library.objects.create(name="Nairobi Central Library")
library1.books.add(book1, book2)

library2 = Library.objects.create(name="Kisumu Public Library")
library2.books.add(book3)

librarian1 = Librarian.objects.create(name="Grace Achieng", library=library1)
librarian2 = Librarian.objects.create(name="Peter Otieno", library=library2)

# --- Task Queries ---

# 1. Query all books by a specific author.
author_name = "Ngugi wa Thiong'o"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(book.title)

# 2. List all books in a library.
library_name = "Nairobi Central Library"
nairobi_library = Library.objects.get(name=library_name)
books_in_nairobi = nairobi_library.books.all()
for book in books_in_nairobi:
    print(book.title)

# 3. Retrieve the librarian for a library.
library_at_kisumu = Library.objects.get(name="Kisumu Public Library")
librarian_at_kisumu = Librarian.objects.get(library=library_at_kisumu)
print(librarian_at_kisumu.name)