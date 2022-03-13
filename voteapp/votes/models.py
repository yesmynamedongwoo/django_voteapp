from django.db import models

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=50, null=False)  #null 이면 안되게 설정
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    # auto_now_add: 레코드가 추가될 때 알아서 입력된 시간이 저장되도록 함
    #defult : 데이터의 기본 값을 설정할수있다.

class Option(models.Model):
    name = models.CharField(max_length=20,null=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False) # 연결된 주제가 삭제되면 연결덴 옵션주제도 모두 삭제됨
    #on_delete속성 : 연관된 데이터가 지워질 때 자기자신은 어떻게 행동할지 결정함
    # CASCADE : 내 데이터도 삭제됨
    # SET_NULL : 관계만 끊어지고 참조가 NULL 로 저장됨
    # DO_NOTHING : 아무것도 안함 (무결성이 꺠질수있어서 권장 안함)

class Vote(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False)
    option = models.ForeignKey(Option,on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)