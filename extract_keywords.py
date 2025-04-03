import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from keybert import KeyBERT
from core.models import Syllabus

# Django 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

# KeyBERT 모델 로딩
kw_model = KeyBERT(model='all-MiniLM-L6-v2')

# 필요하면 필터링 함수
def filter_keywords(keywords):
    cleaned = []
    for kw, score in keywords:
        kw = kw.strip()
        if len(kw) >= 2 and not any(x in kw.lower() for x in ['isbn', 'mail', '031', 'ac', 'kr']):
            cleaned.append((kw, score))
    return cleaned

# 각 강의별 키워드 추출
for s in Syllabus.objects.all():
    print(f"\n📘 강의명: {s.title}")

    # 이미 content는 전처리된 명사로 구성되어 있음
    keyword_input = s.content
    keywords = kw_model.extract_keywords(
        keyword_input,
        keyphrase_ngram_range=(1, 2),  # 1~2단어 조합
        stop_words=None,               # 한글이라서 제거하지 않음
        use_mmr=True,
        diversity=0.7,
        top_n=10
    )

    # 정제
    filtered = filter_keywords(keywords)

    print("🔑 정제된 키워드:")
    for kw, score in filtered:
        print(f"   • {kw} ({score:.4f})")
