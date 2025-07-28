"""
Run this script to execute sample ORM queries that demonstrate:
1) All books by a specific author
2) All books in a library
3) The librarian for a library

Ways to run:
    python manage.py shell < relationship_app/query_samples.py
or run directly as a script:
    python relationship_app/query_samples.py
(just ensure DJANGO_SETTINGS_MODULE below matches your project)
"""

import os
import sys

# Adjust if your Django project name differs
DJANGO_SETTINGS_MODULE = "LibraryProject.settings"

def _bootstrap_django():
    # Allow running the file directly: python relationship_app/query_samples.py
    if not os.environ.get("DJANGO_SETTINGS_MODULE"):
        # Find manage.py’s parent directory (project root)
        here = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(here, os.pardir))
        if project_root not in sys.path:
            sys.path.insert(0, project_root)
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
    import django  # noqa
    django.setup()


def get_books_by_author(author_name):
    """Return a QuerySet of Book objects for the given author name."""
    from relationship_app.models import Book
    return Book.objects.filter(author__name=author_name)


def get_books_in_library(library_name):
    """Return a QuerySet of Book objects contained in the given library."""
    from relationship_app.models import Library
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return Library.objects.none()
    return library.books.all()


def get_librarian_for_library(library_name):
    """Return the Librarian instance (or None) for the given library name."""
    from relationship_app.models import Library
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        return None
    # thanks to related_name="librarian"
    return getattr(library, "librarian", None)


def _maybe_create_demo_data():
    """
    Create minimal demo data if the DB is empty.
    Safe to run repeatedly (idempotent).
    """
    from relationship_app.models import Author, Book, Library, Librarian

    if Author.objects.exists() or Book.objects.exists() or Library.objects.exists():
        return

    # Authors
    a1 = Author.objects.create(name="Chinua Achebe")
    a2 = Author.objects.create(name="Ngũgĩ wa Thiong'o")

    # Books
    b1 = Book.objects.create(title="Things Fall Apart", author=a1)
    b2 = Book.objects.create(title="No Longer at Ease", author=a1)
    b3 = Book.objects.create(title="A Grain of Wheat", author=a2)

    # Library + books
    lib = Library.objects.create(name="Nairobi Central Library")
    lib.books.add(b1, b3)

    # Librarian
    Librarian.objects.create(name="Mary W.", library=lib)


def demo():
    """
    Simple demo prints. Adjust the names to your data if needed.
    """
    print("=== DEMO DATA (created if DB was empty) ===")
    _maybe_create_demo_data()

    print("\n1) Books by author: Chinua Achebe")
    for book in get_books_by_author("Chinua Achebe"):
        print(" -", book)

    print("\n2) Books in library: Nairobi Central Library")
    for book in get_books_in_library("Nairobi Central Library"):
        print(" -", book)

    print("\n3) Librarian for library: Nairobi Central Library")
    librarian = get_librarian_for_library("Nairobi Central Library")
    print(" -", librarian if librarian else "None")


if __name__ == "__main__":
    _bootstrap_django()
    demo()
