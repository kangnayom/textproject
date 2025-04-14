#클러스터 대표 토픽 지정
# >파일명 매핑 실패 assign_representatives.py 파일에서 매핑 
#필요X?
import pandas as pd

# 1. 데이터 불러오기
clustered_df = pd.read_csv("/Users/nayomi/Dev/learning_text/date_csv/clustered_keywords.csv")
syllabus_df = pd.read_csv("/Users/nayomi/Dev/learning_text/date_csv/syllabus_extracted_summary.csv")

# 2. 클러스터별 대표 교과목명 추출
# 파일명 기준으로 교과목명 병합
merged = clustered_df[['파일명', '클러스터']].drop_duplicates()
merged = merged.merge(syllabus_df[['파일명', '교과목명']], on='파일명', how='left')

# 3. 클러스터별로 대표 교과목명 하나만 추출
# 같은 클러스터라도 여러 파일이 있을 수 있으므로 대표 교과목명 1개만 사용
representatives = merged.groupby('클러스터')['교과목명'].first().reset_index()
representatives.columns = ['클러스터', '대표_키워드']

# 4. 저장
representatives.to_csv("/Users/nayomi/Dev/learning_text/date_csv/cluster_representatives.csv", index=False, encoding="utf-8-sig")
print("✅ 클러스터별 대표 키워드(교과목명) 저장 완료!")

