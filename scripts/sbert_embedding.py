#SBERT 임베딩 생성

from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

# 1. 전처리된 CSV 로드
df = pd.read_csv("/Users/nayomi/Dev/myproject/preprocessed_nouns.csv")


# 2. 텍스트 리스트 준비
texts = df['명사목록'].dropna().astype(str).tolist()

# 3. SBERT 모델 로드 (한국어 잘 되는 모델 사용)
model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

# 4. 임베딩 생성
embeddings = model.encode(texts, show_progress_bar=True)

# 5. 저장
np.save("sbert_embeddings.npy", embeddings)
print("✅ SBERT 임베딩 생성 및 저장 완료!")
