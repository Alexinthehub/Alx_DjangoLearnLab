from django.shortcuts import render
from django.http import HttpResponse
from .decorators import role_required

# An example home view that doesn't require a specific role
def home(request):
    return render(request, 'bookshelf/home.html')

# This view is only accessible to users with the 'Admin' role
@role_required('Admin')
def admin_view(request):
    return HttpResponse("Welcome to the Admin page!")

# This view is only accessible to users with the 'Librarian' role
@role_required('Librarian')
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian page!")

# This view is only accessible to users with the 'Member' role
@role_required('Member')
def member_view(request):
    return HttpResponse("Welcome to the Member page!")