# 배포 작업 시 사용하는 파일

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lionsummer.settings")

application = get_wsgi_application()
