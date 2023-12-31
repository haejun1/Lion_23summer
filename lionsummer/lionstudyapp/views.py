from django.shortcuts import render, redirect, get_object_or_404
from .models import Lionstudyapp, Comment
from .forms import LionstudyappForm, CommentForm
from datetime import datetime
from django.contrib import messages
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    articles = Lionstudyapp.objects.all()
    context = {"articles": articles}
    return render(request, "lionstudyapp/index.html", context)


def create(request):
    if request.method == "POST":
        form = LionstudyappForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = datetime.now()
            post.user = request.user
            post.save()
            return redirect("index")
        else:
            messages.error(request, "폼이 유효하지 않습니다.")
    else:
        form = LionstudyappForm()
        return render(request, "lionstudyapp/create.html", {"form": form})
    return render(request, "lionstudyapp/create.html", {"form": form})


def detail(request, pk):
    article = get_object_or_404(Lionstudyapp, pk=pk)
    form = CommentForm()
    context = {"article": article, "form": form}
    return render(request, "lionstudyapp/detail.html", context)


def delete(request, pk):
    post = get_object_or_404(Lionstudyapp, pk=pk)
    if request.user == post.user:
        post.delete()
    return redirect("index")


def update(request, pk):
    post = get_object_or_404(Lionstudyapp, pk=pk)
    if request.user == post.user:
        if request.method == "POST":
            form = LionstudyappForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect("detail", pk=post.pk)
            else:
                messages.error(request, "폼이 유효하지 않습니다.")
        else:
            form = LionstudyappForm(instance=post)
            return render(request, "lionstudyapp/edit.html", {"form": form})
    else:
        return redirect("index")
    return render(request, "lionstudyapp/edit.html", {"form": form})


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Lionstudyapp, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
        return redirect("detail", article.pk)
    else:
        messages.warning(request, "댓글 작성을 위해서는 로그인이 필요합니다.")
        return redirect("accounts:login")
