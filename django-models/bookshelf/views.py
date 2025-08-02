from django.shortcuts import render
from django.http import HttpResponse
from .decorators import role_required

# The home view does not require a specific role
def home(request):
    return render(request, 'bookshelf/home.html')

@role_required('Admin')
def admin_view(request):
    return HttpResponse("Welcome to the Admin page!")

@role_required('Librarian')
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian page!")

@role_required('Member')
def member_view(request):
    return HttpResponse("Welcome to the Member page!")