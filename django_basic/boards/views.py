from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from .models import Board
from users.models import User
from .forms import BoardForm
from tags.models import Tag


def board_list(req):
    all_boards = Board.objects.all().order_by("-id")
    page = int(req.GET.get("p", 1))
    paginator = Paginator(all_boards, 2)

    boards = paginator.get_page(page)
    return render(req, "board_list.html", {"boards": boards})


def board_write(req):
    if not req.session.get("user"):
        return redirect("/users/login/")

    form = BoardForm()
    if req.method == "GET":
        return render(req, "board_write.html", {"form": form})

    if req.method == "POST":
        form = BoardForm(req.POST)
        if form.is_valid():
            board = Board()

            user_id = req.session.get("user")
            writer = User.objects.get(id=user_id)
            board.title = form.cleaned_data["title"]
            board.contents = form.cleaned_data["contents"]
            board.writer = writer
            board.save()

            tags = form.cleaned_data.get("tags").split(",")

            for tag in tags:
                if not tag:
                    continue
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect("/boards/list")


def board_detail(req, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404("게시글을 찾을 수 없습니다.")

    return render(req, "board_detail.html", {"board": board})
