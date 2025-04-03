import pdfplumber
import os
import django
import re
from soynlp.normalizer import repeat_normalize
from soynlp.tokenizer import LTokenizer
from soynlp.word import WordExtractor

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from core.models import Syllabus

pdf_folder = os.path.join(os.path.dirname(__file__), 'date')

def extract_course_title(text):
    """교과목명 ~ 학수번호 사이 텍스트를 과목명으로 추출"""
    match = re.search(r'교과목명\s*(.*?)\s*학수번호', text)
    return match.group(1).strip() if match else None

def preprocess_text(text):
    """한글/영어 명사 기반 전처리"""
    # 한글/영어 단어만 추출
    tokens = re.findall(r'[A-Za-z가-힣]+', text)
    return ' '.join(tokens)

for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        file_path = os.path.join(pdf_folder, filename)

        # PDF 텍스트 추출
        full_text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"

        # 과목명 추출
        course_title = extract_course_title(full_text)
        if not course_title:
            course_title = filename.replace('.pdf', '')  # fallback

        # 전처리된 텍스트 (한글/영어 명사만)
        processed_text = preprocess_text(full_text)

        # DB 저장
        Syllabus.objects.create(
            title=course_title,
            content=processed_text
        )
        print(f"저장 완료: {course_title}")
