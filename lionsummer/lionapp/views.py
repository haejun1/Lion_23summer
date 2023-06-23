from django.shortcuts import render
import random


# Create your views here.
def index(request):  # 함수를 정의하는 경우 request가 항상 첫번째 인자
    return render(request, "index.html")  # 함수의 반환은 render, "index.html"이라는 파일을 반환


def lotto(request):
    pick = random.sample(range(1, 46), 6)
    context = {"pick": pick}
    return render(
        request, "lotto.html", context
    )  # context를 통해 pick을 "lotto.html"에서 쓸 수 있게 함, context는 항상 dictionary(파이썬)이다.
    # html에서 views의 pick을 받으려면 {{ }} 사이에 적어야 한다


def computer(request):
    languages = ["HTML", "CSS", "bootstrap", "django", "python"]
    language = random.choice(languages)
    context = {"language": language, "languages": languages}
    return render(request, "computer.html", context)


def hi(request, name):  # 함수 안에 변수를 쓰려고 name을 적어 인자를 받음
    context = {"name": name}
    # 왼쪽 "name"이 html에서 {{}}안에 적는 문자와 같다, 오른쪽 name이 urls에 받아온 name과 같다
    return render(request, "hi.html", context)


def add(request, a, b):  # 인자 2개 추가도 가능하다
    result = a + b
    context = {"result": result}
    return render(request, "add.html", context)


def posts(request, id):  # url에서 id로 지정했으면 view에서도 id로 지정해야 keyword인자로 작동시킬 수 있다
    content = "Life is short, you need python!"
    replies = ["유익!", "별로야", "많은 정보 얻어가요"]
    no_replies = []
    user = "haejun"
    context = {
        "id": id,
        "replies": replies,
        "no_replies": no_replies,
        "content": content,
        "user": user,
    }
    return render(request, "posts.html", context)


def detail(request):
    test = "block body 사용해보기"
    context = {"test": test}
    return render(request, "detail.html", context)
