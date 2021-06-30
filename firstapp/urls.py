from django.urls import path
from . import views

urlpatterns = [
    path('index1', views.index1),
    path('index2', views.index2),
    path('main', views.main),
    path('insert', views.insert),
    path('show', views.show),
    path('class-view', views.ClassViewExample.as_view()),
    path('show2', views.show2),
    path('template', views.template),
    path('template_extension', views.template_extionsion),
]