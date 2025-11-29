from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings


def role_permission_required(permission_codename):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.error(request, "You must be logged in to access this page.")
                return redirect('/Authentication/login/')
            if request.user.has_permission(permission_codename.split(".")[-1]):
                return view_func(request, *args, **kwargs)
            else:
                messages.error(
                    request, "You do not have permission to access this page."
                )
                return redirect('/Authentication/login/')
        return _wrapped_view

    return decorator