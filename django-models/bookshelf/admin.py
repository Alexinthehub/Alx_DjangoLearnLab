from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile

# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userprofile'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)