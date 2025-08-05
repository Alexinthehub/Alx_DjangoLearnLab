# In advanced_features_and_security/LibraryProject/relationship_app/models.py

from django.db import models
from django.conf import settings  # Import settings to reference the custom user model
from django.db.models.signals import post_save
from django.dispatch import receiver

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book Model with a ForeignKey to Author
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField(null=True, blank=True)

   
    def __str__(self):
        return self.title


# Library Model with a ManyToMany relationship to Book and a ForeignKey to CustomUser
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_libraries',
        null=True,     # Add this line
        blank=True     # Add this line
    )

    def __str__(self):
        return self.name