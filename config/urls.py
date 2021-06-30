from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('firstapp/', include('firstapp.urls')),
    path('admin/', admin.site.urls),
]
