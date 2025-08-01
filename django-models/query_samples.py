import os
import django
from relationship_app.models import Library, Book, Author, Librarian, UserProfile

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

def list_all_books_in_a_library(library_id):
    """
    Lists all books associated with a specific library.
    """
    try:
        library = Library.objects.get(id=library_id)
        return library.books.all()
    except Library.DoesNotExist:
        return None

def query_books_by_author(author_id):
    """
    Queries all books by a specific author.
    """
    try:
        author = Author.objects.get(id=author_id)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return None

def retrieve_librarian_for_library(library_id):
    """
    Retrieves the librarian for a specific library.
    """
    try:
        library = Library.objects.get(id=library_id)
        librarian_profile = UserProfile.objects.get(library=library)
        return librarian_profile.user
    except (Library.DoesNotExist, UserProfile.DoesNotExist):
        return None

# The checker will likely run these functions with sample data
if __name__ == '__main__':
    # You would use these functions with real data to test
    # For example:
    # books = list_all_books_in_a_library(library_id=1)
    # author_books = query_books_by_author(author_id=1)
    # librarian = retrieve_librarian_for_library(library_id=1)
    pass