from django.contrib import admin
from django.urls import path, include  # include를 포함시킴으로 url을 분리할 수 있다

from lionapp import views  # lionapp파일 안에 있는 views를 가져온다

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lionapp/", include("lionapp.urls")),
]
