# delete.md

```python
# Retrieve the book by title
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Try retrieving all books to confirm deletion
Book.objects.all()
```
