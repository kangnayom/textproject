from django.db import models

# Create your models here.
from django.db import models

class Syllabus(models.Model):
    title = models.CharField(max_length=200)  # 예: "데이터베이스와 NoSQL"
    content = models.TextField()              # 전체 추출된 텍스트
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
