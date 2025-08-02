from django.urls import path
from . import views

urlpatterns = [
    path('admin_page/', views.admin_view, name='admin_view'),
    path('librarian_page/', views.librarian_view, name='librarian_view'),
    path('member_page/', views.member_view, name='member_view'),
]