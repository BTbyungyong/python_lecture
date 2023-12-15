from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse

from .models import User
from .forms import LoginForm


def home(req):
    return render(req, "home.html")


def register(req):
    if req.method == "GET":
        return render(req, "register.html")

    if req.method == "POST":
        username = req.POST.get("username", None)
        useremail = req.POST.get("useremail", None)
        password = req.POST.get("password", None)
        re_password = req.POST.get("re-password", None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data["error"] = "모든 값을 입력해야 합니다."
        elif password != re_password:
            res_data["error"] = "비밀번호가 일치하지 않습니다."
        else:
            user = User(
                username=username, useremail=useremail, password=make_password(password)
            )

            user.save()

        return render(req, "register.html", res_data)


def login(req):
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            req.session["user"] = form.user_id
            return redirect("/")

    if req.method == "GET":
        form = LoginForm()

    return render(req, "login.html", {"form": form})
    # if req.method == 'GET':
    #     return render(req,'login.html')

    # if req.method == 'POST':
    #     username = req.POST.get('username',None)
    #     password = req.POST.get('password',None)

    #     res_data = {}
    #     if not (username and password):
    #         res_data['error'] = '아이디와 비밀번호를 입력해 주세요.'
    #     else:
    #         user = User.objects.get(username=username)
    #         if check_password(password,user.password):
    #             req.session['user'] = user.id
    #             return redirect('/')
    #         else:
    #             res_data['error'] = '비밀번호가 일치하지 않습니다.'

    #     return render(req,'login.html',res_data)


def logout(req):
    if req.session.get("user"):
        del req.session["user"]
    return redirect("/")
