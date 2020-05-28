from . import views #.은 현재 폴더(elections)를 의미합니다.
from django.urls import path
from django.contrib import admin


urlpatterns = [
    #path('', views.index),
    path('', views.kibana_page),
    path('login/', views.login),
    path('admin/', admin.site.urls),
    path('executepy/', views.executepy),
    path('dashboardtwo', views.kibana_page2),
]
