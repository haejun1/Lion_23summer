from django.contrib import admin
from django.urls import path
from lionapp import views  # lionapp파일 안에 있는 views를 가져온다

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index),  # index가 들어오면, views안에 있는 index함수를 실행
    path("lotto/", views.lotto),  # 함수에 python써볼 것
    path(
        "computer/", views.computer
    ),  # for문 실습, 인덱스 사용할려면 {[languages.0]}과 같이 써야한다,  ()나 []를 못쓴다
]
