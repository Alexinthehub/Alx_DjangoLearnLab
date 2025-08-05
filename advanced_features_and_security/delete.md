# In the Django Shell

from bookshelf.models import Book
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()
Book.objects.all()

# Expected Output:

# (1, {})

# <QuerySet []>
