from bookshelf.models import Book

# Delete the book instance

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check that it's deleted

Book.objects.all()

# Output:

# <QuerySet []>
