from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password

from .forms import RegisterForm, LoginForm
from .models import User


def index(req):
    return render(req, "index.html", {"email": req.session.get("user")})


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/"

    def form_valid(self, form):
        user = User(
            email=form.data.get("email"),
            password=make_password(form.data.get("password")),
            level="user",
        )
        user.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        self.request.session["user"] = form.data.get("email")
        return super().form_valid(form)


def logout(req):
    if "user" in req.session:
        del req.session["user"]

    return redirect("/")
