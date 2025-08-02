from django.http import HttpResponseForbidden
from functools import wraps

def role_required(role):
    """
    Decorator for views that checks if the user is logged in
    and has a specific role.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Ensure user is authenticated
            if not request.user.is_authenticated:
                return HttpResponseForbidden("You must be logged in to view this page.")

            # Check if the user has a UserProfile and the correct role
            if hasattr(request.user, 'userprofile') and request.user.userprofile.role == role:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You do not have permission to view this page.")
        return _wrapped_view
    return decorator