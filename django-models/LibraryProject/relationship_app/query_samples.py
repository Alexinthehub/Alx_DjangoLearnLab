from relationship_app.models import Author, Book, Library, Librarian

# Create authors
author1 = Author.objects.create(name="George Orwell", birth_date="1903-06-25")
author2 = Author.objects.create(name="Jane Austen", birth_date="1775-12-16")

# Create books and assign authors
book1 = Book.objects.create(title="1984", publication_year=1949)
book1.authors.set([author1])

book2 = Book.objects.create(title="Pride and Prejudice", publication_year=1813)
book2.authors.set([author2])

book3 = Book.objects.create(title="Multi-Author Book", publication_year=2000)
book3.authors.set([author1, author2])

# Create library and assign books
library = Library.objects.create(name="Central Library", location="Downtown")
library.books.set([book1, book2, book3])

# Create librarian and assign library
librarian = Librarian.objects.create(name="Alex Mwendwa", employee_id="EMP001", library=library)

# Output to console
print("Authors:")
for author in Author.objects.all():
    print(f"- {author.name} ({author.birth_date})")

print("\nBooks and their authors:")
for book in Book.objects.all():
    authors = ", ".join([author.name for author in book.authors.all()])
    print(f"- {book.title} ({book.publication_year}) by {authors}")

print("\nLibrary and its books:")
print(f"{library.name} at {library.location}")
for book in library.books.all():
    print(f"  - {book.title}")

print(f"\nLibrarian: {librarian.name} (ID: {librarian.employee_id}) manages {librarian.library.name}")
