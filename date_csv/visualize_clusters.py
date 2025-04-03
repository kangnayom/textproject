#Kmean 추출 결과 시각화
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# 1. CSV 파일 로드
df = pd.read_csv("/Users/nayomi/Dev/learning_text/date_csv/clustered_keywords.csv")

# 2. 필요한 열만 추출
if '클러스터' not in df.columns:
    raise ValueError("❗ '클러스터' 컬럼이 존재하지 않아요!")
if '명사목록' not in df.columns:
    raise ValueError("❗ '명사목록' 컬럼이 존재하지 않아요!")

keywords = df['명사목록']
clusters = df['클러스터']

# 3. 명사 목록 → 텍스트 벡터화 (PCA로 시각화를 위한 차원 축소)
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(keywords.astype(str))

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X.toarray())

# 4. 시각화
plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=clusters, cmap='tab10', alpha=0.7)
plt.title("📌 KMeans 클러스터링 결과 시각화")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.colorbar(scatter, label="클러스터 번호")
plt.grid(True)
plt.tight_layout()
plt.show()
