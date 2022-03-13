from django import forms


class PollCreateForm(forms.Form):
    topic = forms.CharField(label='투표 주제', min_length='2', max_length= '50')  # 차필드는 문자열 , 레이블 태그로 속성을 지정 (사용자에게 보여질 이름
    options = forms.CharField(label='투표 선택 옵션', min_length= '2', max_length= '300')
