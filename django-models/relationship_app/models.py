from django.db import models

<<<<<<< HEAD

class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    # ForeignKey: many books -> one author
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",   # lets us use author.books.all()
    )

    class Meta:
        unique_together = ("title", "author")
        ordering = ["title"]

    def __str__(self) -> str:
        return f"{self.title} — {self.author.name}"


class Library(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # ManyToMany: a library holds many books; a book can be in many libraries
    books = models.ManyToManyField(
        Book,
        related_name="libraries",
        blank=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=255)
    # OneToOne: exactly one librarian per library (and vice‑versa)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        related_name="librarian",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name} @ {self.library.name}"
=======
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    user_name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name
from django.db import models

# Create your models here.
>>>>>>> aea86264ebf01363a67a1d20dbc3f7bce3c4d97b
