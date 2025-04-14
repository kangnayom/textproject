#강의계획서 admin 업로드 및 db저장
from django.db import models

class Syllabus(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
 #시간표모델

class Timetable(models.Model):
    user = models.CharField(max_length=100)  # 로그인 시스템 없으면 그냥 임시로 문자
    subject_name = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=10)  # 예: '월', '화', ...
    period = models.IntegerField()  # 예: 1교시, 2교시 등

    def __str__(self):
        return f"{self.user} - {self.subject_name} ({self.day_of_week} {self.period}교시)"
   
from django.db import models

class SyllabusDetail(models.Model):
    subject_name = models.CharField(max_length=200)
    course_outline = models.TextField(null=True, blank=True)
    course_goal = models.TextField(null=True, blank=True)
    weekly_goals = models.TextField(null=True, blank=True)
    merged_text = models.TextField(null=True, blank=True)
    embedding_path = models.CharField(max_length=255, null=True, blank=True)  # .npy 경로 저장용

    class Meta:
        db_table = 'syllabus_detail'  # MySQL 테이블 이름



class Lecture(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  # 예: '데이터베이스'
    day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=50)

    # ✅ 추가: 강의계획서 기반 텍스트
    syllabus_summary = models.TextField(blank=True, null=True)
    syllabus_keywords = models.TextField(blank=True, null=True)
    sbert_vector_path = models.CharField(max_length=200, blank=True, null=True)  # .npy 파일 경로

    def __str__(self):
        return self.name
    
    # core/models.py
from django.db import models

class SyllabusTable(models.Model):
    subject_name = models.CharField(max_length=255)
    summary_text = models.TextField(blank=True, null=True)  # 추가: 요약 텍스트
    embedding_vector = models.BinaryField(blank=True, null=True)  # 추가: 임베딩 벡터

    class Meta:
        db_table = 'syllabus_table'  # 기존 MySQL 테이블과 동일하게 유지

# core/models.py
class LectureSyllabus(models.Model):
    course_name = models.CharField(max_length=200)
    summary_text = models.TextField()
    embedding_file_path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.course_name


from django.db import models

class LectureEmbedding(models.Model):
    course_name = models.CharField(max_length=200)
    lecture_text = models.TextField()
    embedding = models.BinaryField()

    def __str__(self):
        return self.subject_name
