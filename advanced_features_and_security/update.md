# In the Django Shell

from bookshelf.models import Book
book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
book_to_update

# Expected Output: <Book: Nineteen Eighty-Four>
