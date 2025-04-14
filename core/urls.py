# core/urls.py

from django.urls import path
from . import views
from .views import timetable_register  # 💡 이 줄 추가!

urlpatterns = [
    path('', views.home, name='home'),  # 메인 페이지
    path('syllabus/', views.syllabus_check, name='syllabus_check'),  # syllabus 페이지
    path('timetable/register/', timetable_register, name='timetable_register'),  # 시간표 등록
]
