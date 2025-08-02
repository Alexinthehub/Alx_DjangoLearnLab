from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

@login_required
@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'bookshelf/admin_view.html')

@login_required
@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'bookshelf/librarian_view.html')

@login_required
@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'bookshelf/member_view.html')
