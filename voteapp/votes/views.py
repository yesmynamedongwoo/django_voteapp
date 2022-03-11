from django.http import HttpResponse
from django.shortcuts import render


# import 모듈 안으로 접속속 ctrl + 클릭
# Create your views here.
def view_all_polls(request):
    method = request.method
    name = request.GET.get('name', 'username')
    # (쿼리파라미터,기본값) url 에 name 값이 저장되어있으면 그걸 가져오고 없으면 username를 가져옴
    if method == 'GET':  # GET 일 경우 request get 딕셔녀리 안에 파라미터들이 키 벨류 형태로 담김
        data = request.GET.urlencode()
    elif method == 'POST':  # POST 일 경우 request post 딕셔녀리 안에 파라미터들이 담김
        data = request.POST.urlencode()
        # urlencode 라는 함수를 호출하면 파라미터를 url 형태로 호출해줌

    return HttpResponse("method: %s name: %s" % (method, name))


def create_poll(request):
    return HttpResponse('create')


def view_poll_by_id(request, id):
    return HttpResponse('view poll ' + str(id))


def vote_poll(request, id):
    return HttpResponse('vote poll ' + str(id))


def update_poll(request, id):
    return HttpResponse('update poll ' + str(id))


def delete_poll(request, id):
    return HttpResponse('delete poll ' + str(id))
