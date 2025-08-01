from relationship_app.models import Author, Book, Library, Librarian

# Clean up any existing data to ensure a fresh run
Author.objects.all().delete()
Book.objects.all().delete()
Library.objects.all().delete()
Librarian.objects.all().delete()


# --- Sample Data Creation ---

# 1. Create and save new Authors
author1 = Author.objects.create(name="Chinua Achebe")
author2 = Author.objects.create(name="Ngugi wa Thiong'o")

# 2. Create and save new Books linked to authors (ForeignKey)
book1 = Book.objects.create(title="Things Fall Apart", author=author1)
book2 = Book.objects.create(title="The River Between", author=author2)
book3 = Book.objects.create(title="Weep Not, Child", author=author2)

# 3. Create Libraries and add books to them (ManyToMany)
library1 = Library.objects.create(name="Nairobi Central Library")
library1.books.add(book1, book2)

library2 = Library.objects.create(name="Kisumu Public Library")
library2.books.add(book3)

# 4. Assign Librarians to Libraries (OneToOne)
librarian1 = Librarian.objects.create(name="Grace Achieng", library=library1)
librarian2 = Librarian.objects.create(name="Peter Otieno", library=library2)


# --- Query Samples for the Task ---

print("--- Query all books by a specific author ---")
# Query all books by Ngugi wa Thiong'o
ngugi_books = Book.objects.filter(author__name="Ngugi wa Thiong'o")
for book in ngugi_books:
    print(f"- {book.title}")

print("\n--- List all books in a library ---")
# List all books in the "Nairobi Central Library"
nairobi_library = Library.objects.get(name="Nairobi Central Library")
books_in_nairobi = nairobi_library.books.all()
for book in books_in_nairobi:
    print(f"- {book.title}")

print("\n--- Retrieve the librarian for a library ---")
# Retrieve the librarian for the "Nairobi Central Library"
librarian_at_nairobi = Librarian.objects.get(library__name="Nairobi Central Library")
print(f"- {librarian_at_nairobi.name}")