# 시간표에서 과목명 추출하기
# models.py의 Timetable 모델을 기반으로 과목명 추출하는 기능

import os
import django
import sys
sys.path.append('/Users/nayomi/Dev/learning_text')

# ✅ 경로 설정 (Django root 경로 추가)
sys.path.append("/Users/nayomi/Dev/learning_text")

# ✅ Django 세팅 등록
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

# ✅ 모델 import
from core.models import Timetable

timetables = Timetable.objects.all()
for t in timetables:
    print("사용자:", t.user, "과목명:", t.subject_name)

def extract_subject_names():
    subject_names = []

    timetables = Timetable.objects.all()
    for t in timetables:
        # 엑셀/CSV 파일일 경우를 가정해 pandas로 불러오기
        try:
            df = pd.read_csv(t.file.path)
            # 엑셀이라면: df = pd.read_excel(t.file.path)
        except Exception as e:
            print(f"❌ {t.file.path} 불러오기 실패: {e}")
            continue

        # 셀에서 과목명이 담긴 컬럼명 추측 또는 탐색
        # 예시: '과목명', '강의명', 'Subject' 등이 있다면 그 열 사용
        possible_columns = ['과목명', '강의명', 'Subject', 'subject']
        for col in df.columns:
            if any(key in col for key in possible_columns):
                subject_names += df[col].dropna().unique().tolist()

    subject_names = list(set(subject_names))  # 중복 제거
    print("📘 추출된 과목명 리스트:", subject_names)
    return subject_names

# 실행 예시
if __name__ == "__main__":
    extract_subject_names()
