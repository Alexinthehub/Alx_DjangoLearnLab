# In django-models/relationship_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from .models import Book, Library
from django.contrib.auth.decorators import user_passes_test # Add this import
from .models import UserRole # Add this import


# --- Views from Previous Task ---

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display a specific library's details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# --- Views for Current Task ---

# Function-based view for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Helper functions to check user roles
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == UserRole.ADMIN

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == UserRole.LIBRARIAN

def is_member(user):
    return user.is_authenticated and user.userprofile.role == UserRole.MEMBER


# Role-based view for Admin
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Role-based view for Librarian
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Role-based view for Member
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')