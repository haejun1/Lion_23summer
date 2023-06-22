from django.contrib import admin
from django.urls import path
from lionapp import views  # lionapp파일 안에 있는 views를 가져온다

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index),  # index가 들어오면, views안에 있는 index함수를 실행
    path("lotto/", views.lotto),  # 함수에 python써볼 것
    path("computer/", views.computer),
    # for문 실습, 인덱스 사용할려면 {[languages.0]}과 같이 써야한다,  ()나 []를 못쓴다
    path("hi/<str:name>/", views.hi),
    # variable routing이라 한다. /뒤에 문자나 숫자를 페이지에 반영하는 것, str:name  str로 무슨 값이 들어오든 name이라는 변수로 담아 두겠다
    # 링크에 hi/안녕 이라고 치면 안녕에 오신걸 환영합니다 라고 뜬다
    path("add/<int:a>/<int:b>/", views.add),
    # int a와 int b를 추가하면 a+b가 출력되게 하는 실습, 어따 써먹지?
]
