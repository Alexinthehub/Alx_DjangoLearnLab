from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Helper functions to check for a specific role
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'bookshelf_profile') and user.bookshelf_profile.role == 'Admin'
def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'bookshelf_profile') and user.bookshelf_profile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'bookshelf_profile') and user.bookshelf_profile.role == 'Member'

# Role-specific views with access control
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, 'bookshelf/admin_view.html')

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, 'bookshelf/librarian_view.html')

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render(request, 'bookshelf/member_view.html')