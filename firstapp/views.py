from django.http.response import JsonResponse
from .models import Curriculum
from django.shortcuts import HttpResponse, render
from django.views import generic


def index1(request):
    return HttpResponse('<u>Hello</u>')

def main(request):
    return HttpResponse('<u>Main</u>')

def insert(requset):
    Curriculum(name='linux').save()
    Curriculum(name='python').save()
    Curriculum(name='html/css/js').save()
    Curriculum(name='django').save()

    return HttpResponse('데이터입력 완료')

class ClassViewExample(generic.ListView):
    template_name = 'firstapp/class_view_template.html'
    context_object_name = 'name'

    def get_queryset(self):
        return Curriculum.objects.all()

# http response
def index2(request):
    return HttpResponse('<u>Hi</u>')

# html template response
def show(request):
    curriculum = Curriculum.objects.all()

    return render(
        request, 'firstapp/show.html', 
        {'data': curriculum}
    )

# json response
from django.forms.models import model_to_dict

def show2(request):
    curriculum = Curriculum.objects.all()
    data = []
    for c in curriculum:
        c = model_to_dict(c) # QuerySet -> Dict
        data.append(c)

    # dict가 아닌 자료는 항상 safe=False 옵션 사용
    return JsonResponse(data, safe=False)