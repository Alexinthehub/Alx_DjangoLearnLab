from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'bookshelf/admin_view.html', {'role': 'Admin'})

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'bookshelf/librarian_view.html', {'role': 'Librarian'})

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'bookshelf/member_view.html', {'role': 'Member'})