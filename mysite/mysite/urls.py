"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

#실제 함수가 위치할 파일을 import
from mydjango import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #기본 요청이 왔을 때 mydjango의 views.py 파일의 index 함수가 처리
    path('', views.index),
    #detail/숫자 요청이 오면 views.py 파일의 detail 함수가 처리
    path('detail/<int:itemid>', views.detail),
    path('insert', views.insert)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
