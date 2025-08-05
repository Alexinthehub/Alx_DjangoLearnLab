# In advanced_features_and_security/LibraryProject/relationship_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, Author, Library, CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )


# We will remove the UserProfile model admin since we are replacing it
# with the CustomUser model.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)