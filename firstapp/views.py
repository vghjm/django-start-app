from .models import Curriculum
from django.shortcuts import HttpResponse, render

def index1(request):
    return HttpResponse('<u>Hello</u>')

def index2(request):
    return HttpResponse('<u>Hi</u>')

def main(request):
    return HttpResponse('<u>Main</u>')

def insert(requset):
    # 1. linux 입력
    Curriculum.objects.create(name='linux')

    # 2. python 입력
    c = Curriculum(name='python')
    c.save()

    # 3. html/css/js 입력
    Curriculum(name='html/css/js').save()

    # 4. django 입력
    Curriculum(name='django').save()

    return HttpResponse('데이터입력 완료')

def show(request):
    curriculum = Curriculum.objects.all()

    # response = ''
    # for c in curriculum:
    #     response += c.name + '<br>'

    # return HttpResponse(response)

    return render(
        request, 'firstapp/show.html', 
        {'data': curriculum}
    )
