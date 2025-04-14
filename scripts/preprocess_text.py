#전처리

import pandas as pd
import re
from soynlp.normalizer import repeat_normalize
from soynlp.tokenizer import LTokenizer
from soynlp.word import WordExtractor

# CSV 파일 로드
df = pd.read_csv("/Users/nayomi/Dev/myproject/syllabus_extracted_summary.csv")


# 전처리할 텍스트 컬럼
target_columns = ["교과목명", "수업개요", "수업목표 및 내용", "주차별 학습목표"]

# 모든 텍스트 합쳐서 학습용 말뭉치 생성
corpus = []
for col in target_columns:
    corpus += df[col].fillna("").astype(str).tolist()

# 반복 문자 정규화 및 전처리
def preprocess_text(text):
    text = repeat_normalize(text, num_repeats=2)
    text = re.sub(r"[^\uAC00-\uD7A3a-zA-Z0-9\s]", "", text)  # 한글, 영어, 숫자, 공백만 남기기
    return text

preprocessed_corpus = [preprocess_text(t) for t in corpus if t.strip() != ""]

# 단어 추출기 학습
word_extractor = WordExtractor(min_frequency=2, min_cohesion_forward=0.05)
word_extractor.train(preprocessed_corpus)
word_score_table = word_extractor.extract()

# 토크나이저 생성 후 전처리된 명사 추출
tokenizer = LTokenizer(scores={word: score.cohesion_forward for word, score in word_score_table.items()})

def extract_keywords(text):
    tokens = tokenizer.tokenize(preprocess_text(text))
    return [t for t in tokens if len(t) > 1]

# 각 컬럼에 대해 키워드 추출 후 저장
df_keywords = pd.DataFrame()
df_keywords["파일명"] = df["파일명"]

for col in target_columns:
    df_keywords[col + "_키워드"] = df[col].fillna("").astype(str).apply(lambda x: ", ".join(extract_keywords(x)))

# 결과 저장
df_keywords.to_csv("syllabus_keywords_soynlp.csv", index=False, encoding="utf-8-sig")
print("✅ soynlp 기반 키워드 추출 완료 및 저장 완료!")
