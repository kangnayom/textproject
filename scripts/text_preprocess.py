#pdf파일에서 텍스트 추출


import os
import django
import re
from soynlp.tokenizer import LTokenizer
from soynlp.normalizer import repeat_normalize

# Django 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from core.models import Syllabus

# 토크나이저 초기화
tokenizer = LTokenizer()

# 전처리 함수 (특수문자, 숫자, 줄바꿈 제거)
def clean_text(text):
    text = repeat_normalize(text, num_repeats=2)
    text = re.sub(r"[^가-힣\s]", " ", text)   # 한글, 공백만 남기기
    text = re.sub(r"\s+", " ", text)         # 여러 공백 → 하나
    return text.strip()

# 명사 추출 함수
def extract_nouns(text):
    tokens = tokenizer.tokenize(text)
    nouns = [tok for tok in tokens if len(tok) > 1 and not tok.isdigit()]
    return nouns

# 모든 Syllabus 데이터 전처리 실행
for s in Syllabus.objects.all():
    cleaned = clean_text(s.content)
    nouns = extract_nouns(cleaned)
    
    print(f"\n📘 {s.title}")
    print("🔍 명사 추출 결과 (샘플):", nouns[:20])
