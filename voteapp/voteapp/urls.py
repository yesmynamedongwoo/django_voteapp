"""voteapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from votes import views


urlpatterns = [  #url 패턴이라는 튜플
    path('polls/', views.view_all_polls),
    path('polls/create',views.create_poll),
    path('polls/<int:id>/', views.view_poll_by_id),
    path('polls/<int:id>/vote', views.vote_poll),
    path('polls/<int:id>/update/', views.update_poll),
    path('polls/<int:id>/delete/', views.delete_poll),
    # <> 장고에서 경로 파라미터의 시작과 끝  경로에서 저 사이의 값을 인트형으로 변환해 전달   예시 ) <int:id> , <str:id>
]
