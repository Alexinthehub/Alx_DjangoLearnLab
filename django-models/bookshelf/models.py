from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='userprofile')
    role = models.CharField(max_length=10, choices=ROLES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"