from . import views #.은 현재 폴더(elections)를 의미합니다.
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('admin/', admin.site.urls),
    path('start/', views.kibana_page),
    path('executepy/', views.executepy),
]
