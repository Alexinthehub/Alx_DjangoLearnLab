# In LibraryProject/bookshelf/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm 

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """
    A view to demonstrate secure form handling for creating a new book.
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookshelf:book_list') # Updated line
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})