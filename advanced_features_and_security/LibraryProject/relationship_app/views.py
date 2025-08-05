# In LibraryProject/relationship_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.forms import ModelForm


# All data access is performed using Django's ORM, which automatically
# escapes user input and prevents SQL injection attacks.
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('relationship_app:book_list')
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Create'})

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('relationship_app:book_list')
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Update'})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('relationship_app:book_list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})