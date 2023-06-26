from django.shortcuts import render, redirect
from .models import Lionstudyapp


# Create your views here.
def index(request):
    return render(request, "lionstudyapp/index.html")


def new(request):
    return render(request, "lionstudyapp/new.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    article = Lionstudyapp(title=title, content=content)
    article.save()
    return redirect("/")
