"""
ASGI config for voteapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
# wsgi 의 업그레이드 버전 비동기도 지원
# 웹서버에 동시접속이 많아지면 파이썬으로 처리하기 어렵기때문에 미들웨어를 사용해주어야함.
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voteapp.settings')

application = get_asgi_application()
