from django.urls import path
from . import views

urlpatterns = [
    # lionapp/index 식으로 작성해야 함
    # app당 url을 만들어서 관리하기 위함
    path("index/", views.index),  # index가 들어오면, views안에 있는 index함수를 실행
    path("lotto/", views.lotto),  # 함수에 python써볼 것
    path("computer/", views.computer),
    # for문 실습, 인덱스 사용할려면 {[languages.0]}과 같이 써야한다,  ()나 []를 못쓴다
    path("hi/<str:name>/", views.hi),
    # variable routing이라 한다. /뒤에 문자나 숫자를 페이지에 반영하는 것, str:name  str로 무슨 값이 들어오든 name이라는 변수로 담아 두겠다
    # 링크에 hi/안녕 이라고 치면 안녕에 오신걸 환영합니다 라고 뜬다
    path("add/<int:a>/<int:b>/", views.add),
    # int a와 int b를 추가하면 a+b가 출력되게 하는 실습, 어따 써먹지?
    path("posts/<int:id>/", views.posts),
    # variable값인 id를 넣으면 숫자를 하나하나 적을 필요가 없다
    path("detail/", views.detail),
    # DTL, ejs처럼 head등 반복되는 것 생략
]
