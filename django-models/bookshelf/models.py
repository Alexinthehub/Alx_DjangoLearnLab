from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define the UserProfile model with a role field
class UserProfile(models.Model):
    ROLES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    # Add a related_name to resolve the conflict
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bookshelf_profile')
    role = models.CharField(max_length=20, choices=ROLES, default='Member')

    def __str__(self):
        return f'{self.user.username} - {self.role}'

# Django Signal to automatically create a UserProfile for new users
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.bookshelf_profile.save() # Use the new related_name here