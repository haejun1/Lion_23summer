from django.shortcuts import render, redirect, get_object_or_404
from .models import Lionstudyapp
from .forms import LionstudyappForm


# Create your views here.
def index(request):
    articles = Lionstudyapp.objects.all()
    context = {"articles": articles}
    return render(request, "lionstudyapp/index.html", context)


def new(request):
    return render(request, "lionstudyapp/create.html")


def create(request):
    if request.method == "POST":
        form = LionstudyappForm(request.POST)
        if form.is_valid():
            form = form.save()
            # form되는지 확인
            return redirect("/")
            # 확인
    else:
        form = LionstudyappForm()
    context = {"form": form}
    return render(request, "lionstudyapp/new.html", context)


def detail(request, pk):
    article = get_object_or_404(Lionstudyapp, pk=pk)
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
