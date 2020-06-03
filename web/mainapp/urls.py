from . import views #.은 현재 폴더(elections)를 의미합니다.
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', views.login),
    path('dashboard/', views.kibana_page),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('dashboardtwo/',views.kibana_page2),
=======
    path('executepy/', views.executepy),
    path('dashboardtwo', views.kibana_page2),
>>>>>>> fcb6b4a260084225316d58fd49581f59163be104
]
