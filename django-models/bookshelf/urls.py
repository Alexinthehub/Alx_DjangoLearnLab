from django.urls import path
from . import views

urlpatterns = [
    # General home page view
    path('', views.home, name='home'),

    # Role-based views
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]