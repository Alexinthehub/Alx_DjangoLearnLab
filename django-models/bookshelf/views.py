from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

# Role-checking functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Views for each role
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'bookshelf/admin_view.html')


@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, 'bookshelf/librarian_view.html')  


@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'bookshelf/member_view.html')
