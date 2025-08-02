from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from bookshelf.models import UserProfile
import os

class Command(BaseCommand):
    help = 'Creates a superuser and ensures a corresponding UserProfile exists with the Admin role.'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'adminpass')

        user, created = User.objects.get_or_create(
            username=username,
            defaults={'email': email, 'is_staff': True, 'is_superuser': True}
        )

        if created:
            user.set_password(password)
            user.save()
            UserProfile.objects.create(user=user, role='Admin')
            self.stdout.write(self.style.SUCCESS('Successfully created admin user and profile!'))
        else:
            self.stdout.write(self.style.SUCCESS('Admin user already exists. Skipping creation.'))