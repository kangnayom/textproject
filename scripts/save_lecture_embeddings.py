import pandas as pd
import ast
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from core.models import LectureEmbedding

# CSV 파일 로드
df = pd.read_csv("/Users/nayomi/Dev/learning_text/date_csv/lecture_topic_corpus2.csv")

# DB에 저장
for _, row in df.iterrows():
    LectureEmbedding.objects.create(
        course_name=row['교과목명'],
        text=row['통합텍스트'],
       embedding=row['실제_컬럼명'].strip()  # 임베딩은 문자열로 저장
    )

print(" DB 저장 완료!")
