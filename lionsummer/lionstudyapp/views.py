from django.shortcuts import render, redirect
from .models import Lionstudyapp


# Create your views here.
def index(request):
    articles = Lionstudyapp.objects.all()
    context = {"articles": articles}
    return render(request, "lionstudyapp/index.html", context)


def new(request):
    return render(request, "lionstudyapp/new.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    article = Lionstudyapp(title=title, content=content)
    article.save()
    return redirect("/")


def detail(request, pk):
    article = Lionstudyapp.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "lionstudyapp/detail.html", context)


def delete(request, pk):
    article = Lionstudyapp.objects.get(pk=pk)
    article.delete()
    return redirect("/")


def edit(request, pk):
    article = Lionstudyapp.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "lionstudyapp/edit.html", context)


def update(request, pk):
    article = Lionstudyapp.objects.get(pk=pk)
    title = request.GET.get("title")
    content = request.GET.get("content")
    article.title = title
    article.content = content
    article.save()

    return redirect(f"/{article.pk}/")
