from django.contrib import admin
from django.urls import path
from lionapp import views  # lionapp파일 안에 있는 views를 가져온다

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index),  # index가 들어오면, views안에 있는 index함수를 실행
]
