# In LibraryProject/bookshelf/forms.py

from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    A sample form for demonstrating form-based security practices.
    """
    class Meta:
        model = Book
        fields = ['title']