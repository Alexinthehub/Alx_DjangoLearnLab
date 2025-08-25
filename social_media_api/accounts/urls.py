# accounts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, CustomAuthToken, UserProfileView, UserViewSet

# Create a router for the UserViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

# Define urlpatterns for registration, login, and profile
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('', include(router.urls)), # Include the router's URLs
]