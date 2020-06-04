from . import views #.은 현재 폴더(elections)를 의미합니다.
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', views.Login),
    path('dashboard/', views.kibana_page),
    path('admin/', admin.site.urls),
    path('dashboardtwo/',views.kibana_page2),
    path('Login/',views.Login),
    path('Logout/',views.Logout),
]