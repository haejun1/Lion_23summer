from django.shortcuts import render, redirect, get_object_or_404
from .models import Lionstudyapp
from .forms import LionstudyappForm
from datetime import datetime
from django.contrib import messages


# Create your views here.
def index(request):
    articles = Lionstudyapp.objects.all()
    context = {"articles": articles}
    return render(request, "lionstudyapp/index.html", context)


def create(request):
    if request.method == "POST":
        form = LionstudyappForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = datetime.now()
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
    context = {"article": article}
    return render(request, "lionstudyapp/detail.html", context)


def delete(request, pk):
    post = get_object_or_404(Lionstudyapp, pk=pk)
    post.delete()
    return redirect("index")


def update(request, pk):
    post = get_object_or_404(Lionstudyapp, pk=pk)
    if request.method == "POST":
        form = LionstudyappForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("detail", pk=post.pk)
        else:
            messages.error(request, "폼이 유효하지 않습니다.")
    else:
        form = LionstudyappForm(instance=post)
        return render(request, "lionstudyapp/edit.html", {"form": form})
    return render(request, "lionstudyapp/edit.html", {"form": form})
