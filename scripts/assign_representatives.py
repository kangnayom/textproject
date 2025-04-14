#클러스트 대표 토픽 지정
#파일-교과목 매팡 할당을 위한 코드
#필요X?

import pandas as pd

# 1. 데이터 로드
clustered_df = pd.read_csv("date_csv/clustered_keywords.csv")
syllabus_df = pd.read_csv("date_csv/syllabus_extracted_summary.csv")

# 2. 클러스터별 대표 키워드 딕셔너리 초기화
cluster_representatives = {}

# 3. 각 클러스터에서 대표 교과목명 추출
for cluster in clustered_df['클러스터'].unique():
    cluster_data = clustered_df[clustered_df['클러스터'] == cluster]
    file_names = cluster_data['파일명'].dropna().unique()

    for fname in file_names:
        matched_row = syllabus_df[syllabus_df['파일명'] == fname]
        if not matched_row.empty:
            subject_name = matched_row.iloc[0]['교과목명']
            if pd.notna(subject_name) and subject_name.strip() != "":
                cluster_representatives[cluster] = subject_name.strip()
                break  # 하나만 매칭되면 바로 대표로 설정

# 4. 결과 저장
output_df = pd.DataFrame([
    {"클러스터": k, "대표 키워드(교과목명)": v}
    for k, v in cluster_representatives.items()
])
output_df.to_csv("date_csv/cluster_representatives.csv", index=False, encoding="utf-8-sig")

print("✅ 클러스터별 대표 키워드(교과목명) 저장 완료!")
