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

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS('Admin user already exists. Skipping creation.'))
            return

        self.stdout.write(f'Creating superuser "{username}"...')

        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )

        # Use get_or_create to safely create or retrieve the UserProfile
        user_profile, created = UserProfile.objects.get_or_create(
            user=user,
            defaults={'role': 'Admin'}
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created admin user and profile!'))
        else:
            self.stdout.write(self.style.SUCCESS('Successfully retrieved existing admin user and profile!'))