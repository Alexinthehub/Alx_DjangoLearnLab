import os
import django
from relationship_app.models import Library, Book, UserProfile

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
    # This query assumes an 'Author' model exists
    # The provided models do not have an Author model directly
    # This function may need to be adjusted based on your final models
    return Book.objects.filter(author_id=author_id)

def retrieve_librarian_for_library(library_id):
    """
    Retrieves the librarian for a specific library.
    """
    try:
        librarian_profile = UserProfile.objects.get(
            role=UserProfile.LIBRARIAN,
            library__id=library_id
        )
        return librarian_profile.user
    except UserProfile.DoesNotExist:
        return None

if __name__ == '__main__':
    pass