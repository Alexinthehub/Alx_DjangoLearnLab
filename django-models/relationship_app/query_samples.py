from relationship_app.models import Author, Book, Library, Librarian
from datetime import date

# Clear previous entries (optional during development)
Author.objects.all().delete()
Book.objects.all().delete()
Library.objects.all().delete()
Librarian.objects.all().delete()

# Create authors
author1 = Author.objects.create(name="George Orwell", birth_date=date(1903, 6, 25))
author2 = Author.objects.create(name="Jane Austen", birth_date=date(1775, 12, 16))

# Create books and assign authors
book1 = Book.objects.create(title="1984", publication_year=1949)
book1.authors.set([author1])

book2 = Book.objects.create(title="Pride and Prejudice", publication_year=1813)
book2.authors.set([author2])

book3 = Book.objects.create(title="Multi-Author Book", publication_year=2000)
book3.authors.set([author1, author2])  # Multiple authors

# Create a library
library = Library.objects.create(name="Central Library", location="Downtown")

# Add books to library
library.books.add(book1, book2, book3)

# Create a librarian assigned to the library
librarian = Librarian.objects.create(name="Alex Mwendwa", employee_id="EMP001", library=library)

# Verify entries
print("Authors:")
for author in Author.objects.all():
    print(f"- {author.name} ({author.birth_date})")

print("\nBooks and their authors:")
for book in Book.objects.all():
    author_names = ', '.join([a.name for a in book.authors.all()])
    print(f"- {book.title} ({book.publication_year}) by {author_names}")

print("\nLibrary and its books:")
print(f"{library.name} at {library.location}")
for book in library.books.all():
    print(f"  - {book.title}")

print(f"\nLibrarian: {librarian.name} (ID: {librarian.employee_id}) manages {librarian.library.name}")
