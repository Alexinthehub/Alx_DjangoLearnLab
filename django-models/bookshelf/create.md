# create.md

```python
# Open Django shell
python manage.py shell

# Inside the shell:
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
```
