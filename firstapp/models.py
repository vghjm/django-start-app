from django.db import models
from django.db.models.query import QuerySet


# 모든 모델은 Manager을 가져야 하며 매니저속성을 정의하지 않는 경우 기본으로 object 속성을 가짐
class SecondManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(name__contains='kim')


# 모델의 기능 연습
class ModelFunctionTest:
    def test(self):
        # 전체 데이터 조회
        Curriculum.objects.all()

        # 데이터 조회 1개
        Curriculum.objects.get(id=2)
        Curriculum.objects.get(name='python')
        Curriculum.objects.get(pk=1)

        # 데이터 조회 N개
        Curriculum.objects.filter(name__contains='go')

        # 데이터 제외 N개
        Curriculum.objects.exclude(name='python')
        Curriculum.objects.exclude(pk=3)

        # 데이터 개수
        Curriculum.objects.count()

        # 정렬
        Curriculum.objects.filter(name__contains='n').order_by('id')
        Curriculum.objects.filter(name__contains='n').order_by('-id') # 내림차순

        # 처음 데이터 조회
        Curriculum.objects.order_by('id').first()

        # 마지막 데이터 조회
        Curriculum.objects.order_by('id').last()

        # 데이터 입력
        Curriculum.objects.create(name='즉시 생성')
        c = Curriculum(name='나중에 생성')
        c.save()

        # 데이터 수정
        data = Curriculum.objects.get(id=2)
        data.name = 'javascript'
        data.save()

        # 데이터 삭제
        data = Curriculum.objects.get(id=3)
        data.delete()




class Curriculum(models.Model):
    name = models.CharField(max_length=255)

    objects = models.Manager()
    second_objects = SecondManager()

    def __str__(self) -> str:
        return self.name
