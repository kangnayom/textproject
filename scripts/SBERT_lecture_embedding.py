#통합테스트 컬럽 sbert로 임베딩해서 저장하는 로직

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# 1. CSV 파일 불러오기
df = pd.read_csv("/Users/nayomi/Dev/learning_text/date_csv/lecture_topic_corpus.csv")

# 2. 텍스트 리스트 만들기 (컬럼 이름이 '통합텍스트'일 경우)
texts = df['통합텍스트'].dropna().astype(str).tolist()

# 3. SBERT 모델 로드 (한국어 전용 모델)
model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

# 4. 임베딩 생성
embeddings = model.encode(texts, show_progress_bar=True)

# 5. 임베딩 저장
np.save("lecture_embeddings.npy", embeddings)
print("✅ SBERT 임베딩 저장 완료!")

# (선택) 원본 CSV도 함께 저장
df.to_csv("lecture_topic_corpus_with_embedding.csv", index=False, encoding='utf-8-sig') 