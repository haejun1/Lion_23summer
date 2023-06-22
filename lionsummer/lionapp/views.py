from django.shortcuts import render


# Create your views here.
def index(request):  # 함수를 정의하는 경우 request가 항상 첫번째 인자
    return render(request, "index.html")  # 함수의 반환은 render, "index.html"이라는 파일을 반환


def lotto(request):
    import random

    pick = random.sample(range(1, 46), 6)
    context = {"pick": pick}
    return render(
        request, "lotto.html", context
    )  # context를 통해 pick을 "lotto.html"에서 쓸 수 있게 함, context는 항상 dictionary(파이썬)이다.
    # html에서 views의 pick을 받으려면 {{ }} 사이에 적어야 한다
