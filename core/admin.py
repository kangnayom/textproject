from django.contrib import admin
from .models import Syllabus

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ['title']             # ✅ 이렇게 리스트 형식으로!
    search_fields = ['title']            # ✅ 반드시 리스트나 튜플로 작성해야 해!


#시간표
from django.contrib import admin
from .models import Timetable

admin.site.register(Timetable)

