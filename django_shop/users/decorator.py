from django.shortcuts import redirect
from .models import User


def login_required(func):
    def wrap(request, *args, **kwargs):
        user = request.session.get("user")
        if user is None or not user:
            return redirect("/login/")
        return func(request, *args, **kwargs)

    return wrap


def admin_required(func):
    def wrap(request, *args, **kwargs):
        user_email = request.session.get("user")
        if user_email is None or not user_email:
            return redirect("/login/")
        user = User.objects.get(email=user_email)
        if user.level != "admin":
            return redirect("/")
        return func(request, *args, **kwargs)

    return wrap
