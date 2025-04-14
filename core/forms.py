from django import forms
from .models import Timetable

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['user', 'subject_name', 'day_of_week', 'period']

#시간표 등록폼
from django import forms
from .models import Timetable

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['user', 'subject_name', 'day_of_week', 'period']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'learning_db',
        'USER': 'nayomi',
        'PASSWORD': 'skdus1023',  # 너가 지정한 비밀번호
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
