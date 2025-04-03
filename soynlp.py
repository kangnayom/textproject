import os
import django
import re
from soynlp.tokenizer import LTokenizer
from soynlp.normalizer import repeat_normalize

# Django 환경 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from core.models import Syllabus

# 간단한 토크나이저 (빈도 기반 토큰으로 바꿔도 돼!)
tokenizer = LTokenizer()

def clean_text(text):
    # 반복 문자 정규화 (ㅋㅋㅋㅋ → ㅋㅋ)
    text = repeat_normalize(text, num_repeats=2)
    # 특수문자 제거
    text = re.sub(r"[^가-힣\s]", " ", text)
    # 줄바꿈/여러 공백 제거
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_nouns(text):
    tokens = tokenizer.tokenize(text)
    nouns = [tok for tok in tokens if len(tok) > 1 and not tok.isdigit()]
    return nouns

# 전체 강의계획서 전처리 실행
for s in Syllabus.objects.all():
    cleaned = clean_text(s.content)
    nouns = extract_nouns(cleaned)
    print(f"\n📘 {s.title}")
    print("🔍 추출된 명사 샘플:", nouns[:20])

