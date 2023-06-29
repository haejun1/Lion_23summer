from django.contrib import admin
from django.urls import path, include  # include를 포함시킴으로 url을 분리할 수 있다
from django.conf.urls.static import static
from django.conf import settings
from lionapp import views  # lionapp파일 안에 있는 views를 가져온다
from lionstudyapp import views

# app 여러개 사용 시 주의할점
# 각 app의 views에서 html을 반환할 때 동일한 이름의 html이 있다면
# 위쪽에 등록된 app의 html부터 반환됨
# 경로 명에 app명을 추가해주면 됨
# ex) render(request, 'lionapp/index.html')

# 반대로 base.html을 각각의 app에서 다 활용하고 싶다면
# settings의 DIRS를 추가

urlpatterns = [
    path("admin/", admin.site.urls),
    path("lionapp/", include("lionapp.urls")),
    path("", include("lionstudyapp.urls")),
    path("accounts/", include("accounts.urls")),
    path("maps/", include("maps.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
