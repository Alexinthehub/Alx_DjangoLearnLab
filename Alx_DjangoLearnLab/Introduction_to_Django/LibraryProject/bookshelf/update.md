# update.md

```python
# Retrieve the book by title
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
print(book.title)
```
