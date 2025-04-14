#강의계획서 SBERT 입력용 텍스트
# 4개컬럼 한줄로 


import pandas as pd

# 파일 경로 설정
input_path = "date_csv/syllabus_extracted_summary.csv"
output_path = "lecture_topic_corpus.csv"

# 데이터 로드
df = pd.read_csv(input_path)

# 텍스트 통합
df["통합텍스트"] = (
    "과목명: " + df["교과목명"].fillna('') + " | " +
    "개요: " + df["수업개요"].fillna('') + " | " +
    "목표: " + df["수업목표 및 내용"].fillna('') + " | " +
    "주차별목표: " + df["주차별 학습목표"].fillna('')
)

# 필요한 컬럼만 저장
df_output = df[["교과목명", "통합텍스트"]]
df_output.to_csv(output_path, index=False, encoding="utf-8-sig")

print("✅ 강의별 텍스트 정리 완료! →", output_path)
