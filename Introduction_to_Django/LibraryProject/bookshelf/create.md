# create.md

```python
# Open Django shell
python manage.py shell

# Inside the shell:
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
```

---

### 📄 `retrieve.md`

````markdown
# retrieve.md

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title)
print(book.author)
print(book.publication_year)


## Retrieve
Book.objects.get(title="1984")

## Update
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

## Delete
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
```
````
