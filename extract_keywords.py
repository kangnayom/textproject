import os
import django
import re
from keybert import KeyBERT

# 1. Django 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from core.models import Syllabus

# 2. 모델 로드
kw_model = KeyBERT(model="all-MiniLM-L6-v2")


# ✅ 3. 교과목명 추출 함수 (학수번호 제거 포함)
def extract_lecture_title(text):
    match = re.search(r"교과목명\s*([가-힣A-Za-z0-9\s&]+)", text)
    if match:
        title = match.group(1).strip()
        title = title.split("학수번호")[0].strip()
        return title
    return "제목없음"


# ✅ 4. 본문 내용 추출 함수 ('강의 개요', '강의 목표' 등 이후부터)
def extract_main_content(text):
    match = re.search(r"(강의\s*(개요|목표|내용))", text)
    if match:
        return text[match.start():]
    return text


# ✅ 5. 키워드 추출 함수 (KeyBERT 사용)
def extract_keywords(text, top_n=20):
    return kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 3),
        stop_words=None,
        use_mmr=True,
        diversity=0.7,
        top_n=top_n
    )


# ✅ 6. 이상한 키워드 필터링 함수
def filter_keywords(keywords):
    cleaned = []
    for kw, score in keywords:
        kw = kw.strip()
        if re.match(r"^[가-힣a-zA-Z\s]{2,}$", kw) and not re.search(
            r"\d|isbn|mail|ac|kr|@|\.", kw.lower()
        ):
            cleaned.append((kw, score))
    return cleaned


# ✅ 7. 전체 실행
for s in Syllabus.objects.all():
    print(f"\n📘 파일명: {s.title}")

    lecture_title = extract_lecture_title(s.content)
    main_text = extract_main_content(s.content)

    raw_keywords = extract_keywords(main_text)
    filtered = filter_keywords(raw_keywords)

    print(f"📌 강의명 추출 결과: {lecture_title}")
    print("🔑 정제된 키워드:")
    for kw, score in filtered[:10]:
        print(f"   • {kw} ({score:.4f})")
