from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import PollCreateForm

# import 모듈 안으로 접속속 ctrl + 클릭
# Create your views here.



def view_all_polls(request):
    context = {
      'topics' : [
          {'id': 1, 'topic': '부먹 vs 찍먹' },
          {'id': 2, 'topic': '김치찌개 vs 된장찌개'},
          {'id': 3, 'topic': '커피 vs 차'}
      ]
    }
    return render(request, 'pages/view_all_polls.html', context)


def create_poll(request):
    if request.method == 'POST':
        form = PollCreateForm(request.POST)
        if form.is_valid(): # is_valid 란?  해당 폼의 clean()을 호출해서 유효성 검사
            print(form.cleaned_data['topic'])
            #데이터베이스에 저장하는 로직 추가 필요
            return HttpResponseRedirect('/polls/')
    else:
        form = PollCreateForm()
    context = {
        'create_form': form
    }

    return render(request, 'pages/create_poll.html', context)


def view_poll_by_id(request, id):
    return HttpResponse('view poll ' + str(id))


def vote_poll(request, id):
    return HttpResponse('vote poll ' + str(id))


def update_poll(request, id):
    return HttpResponse('update poll ' + str(id))


def delete_poll(request, id):
    return HttpResponse('delete poll ' + str(id))


# def view_all_polls(request):
#     method = request.method
#     name = request.GET.get('name', 'username')
#     # (쿼리파라미터,기본값) url 에 name 값이 저장되어있으면 그걸 가져오고 없으면 username를 가져옴
#     if method == 'GET':  # GET 일 경우 request get 딕셔녀리 안에 파라미터들이 키 벨류 형태로 담김
#         data = request.GET.urlencode()
#     elif method == 'POST':  # POST 일 경우 request post 딕셔녀리 안에 파라미터들이 담김
#         data = request.POST.urlencode()
#         # urlencode 라는 함수를 호출하면 파라미터를 url 형태로 호출해줌
#
#     return HttpResponse("method: %s name: %s" % (method, name))

