import pdfplumber
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from core.models import Syllabus
pdf_folder = os.path.join(os.path.dirname(__file__), 'date')

for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        file_path = os.path.join(pdf_folder, filename)

        #PDF 텍스트 추출
        full_text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"

        # DB 저장 (파일명을 제목으로 사용)
        title = filename.replace('.pdf', '')
        Syllabus.objects.create(title=title, content=full_text)
        print(f"저장 완료: {title}")
