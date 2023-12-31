from pathlib import Path
import os

# 기본경로
BASE_DIR = Path(__file__).resolve().parent.parent

# 암호화된 키
SECRET_KEY = "django-insecure-(bp_w)!zt68$i70n&a(l(z#xdfh_npch4elrku!m@p#wsjg46b"

# 개발모드여서 디버그 사용중, 오류 표현을 쉽게 볼 수 있다
DEBUG = True

# * 모든 확장자 파일 허용
ALLOWED_HOSTS = ["*"]


#
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "lionapp",
    "lionstudyapp",
    "accounts",
    "maps",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    # form 태그에서 POST로 보낼 때, 해킹을 방지하기 위한 csrf_token 기능을 수행
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lionsummer.urls"

# 템플릿
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # BTL 엔진을 쓴다는 것
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        # 괄호안에는 경로를 적음, BASE_DIR은 최상위 위치, 경로 추가
        "APP_DIRS": True,
        # templates 폴더 안의 html 파일들을 렌더 가능하게 한다
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            # context처리를 유용하게 한다 (html에서 import안 써도 되게 함)
        },
    },
]

WSGI_APPLICATION = "lionsummer.wsgi.application"


# 데이터베이스
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# PASSWORD 설정
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# 언어
LANGUAGE_CODE = "ko-kr"

# 시간
TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "images"
