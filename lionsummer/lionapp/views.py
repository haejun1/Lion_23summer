from django.shortcuts import render


# Create your views here.
def index(request):  # 함수를 정의하는 경우 request가 항상 첫번째 인자
    return render(request, "index.html")  # 함수의 반환은 render, "index.html"이라는 파일을 반환
