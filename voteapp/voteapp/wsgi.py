"""
WSGI config for voteapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
# 클라이언트 -> 스위치 (로드벨런스),웹서버미들웨어(아파치) -> 장고 (웹 어플리케이션 -> 데이터베이스 (서버 프로그램)
# 아파치 와 같은 웹 미들웨어와 소통하기위한 파일 (웹 서버 게이트웨이 인터페이스)
# 웹서버를 장고 로 바로 킬 수는 있지만
# 웹서버에 동시접속이 많아지면 파이썬으로 처리하기 어렵기때문에 미들웨어를 사용해주어야함.
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voteapp.settings')

application = get_wsgi_application()
