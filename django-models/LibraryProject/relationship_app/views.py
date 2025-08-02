from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from .models import UserProfile

def check_role(required_role):
    def decorator(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == required_role
    return decorator

@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
