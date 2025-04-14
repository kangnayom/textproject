#Kmeans 군집화
#필요 X?
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

# 1. 전처리된 명사 CSV 불러오기 (파일명 포함)
df = pd.read_csv("date_csv/preprocessed_nouns.csv")

# 2. 임베딩 불러오기
embeddings = np.load("date_csv/sbert_embeddings.npy")

# 3. 클러스터 수 정의 (예: 5개)
n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
clusters = kmeans.fit_predict(embeddings)

# 4. 클러스터 결과 저장
df['클러스터'] = clusters

# 5. 저장 (파일명, 명사목록, 클러스터)
df.to_csv("date_csv/clustered_keywords.csv", index=False, encoding="utf-8-sig")

print("✅ KMeans 클러스터링 완료 및 저장 완료!")
