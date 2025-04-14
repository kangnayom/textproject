#1. 엑셀파일 CSV변환후 저장(date_xlsx)
#2. 강의계획서 원본 CSV 중 교과목명, 수업개요, 목표, 주차별 4가지 추출(extract_syllabus_date)
#3. 추출 후 syllabus_extracted_summary.csv 파일로 저장

import os
import pandas as pd
import re

folder_path = "date_xlsx"
summary_data = []

for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path, header=None)

        subject_name = None
        course_outline = None
        course_goal = None
        weekly_goals = []

        # DataFrame을 문자열로 이어붙여 한 줄씩 검색
        lines = df.fillna("").astype(str).apply(lambda row: ','.join(row), axis=1).tolist()

        # 1. 교과목명 추출
        for line in lines:
            if "교과목명" in line and "학수번호" in line:
                subject_name = line.split("교과목명")[-1].split("학수번호")[0].strip(', ').strip()
                break

        # 2. 수업개요 추출
        for idx, line in enumerate(lines):
            if "수업개요" in line:
                next_line = lines[idx + 1] if idx + 1 < len(lines) else ""
                if "수업목표" not in next_line:
                    course_outline = next_line.strip(', ').strip()
                break

        # 3. 수업목표 및 내용 추출
        for line in lines:
            if "수업목표 및 내용" in line or "수업목표" in line:
                parts = line.split("내용")
                if len(parts) > 1:
                    course_goal = parts[-1].strip(', ').strip()
                else:
                    course_goal = line.split("수업목표")[-1].strip(', ').strip()
                break

        # 4. 주차별 학습목표 추출 (숫자로 시작하는 줄만, '연구실' 나오면 종료)
        in_weeks = False
        for line in lines:
            if re.match(r'^\s*\d{2}', line):
                in_weeks = True
            if in_weeks:
                if "연구실" in line:
                    break
                if re.match(r'^\s*\d{2}', line):
                    weekly_goals.append(line.strip())

        summary_data.append({
            "파일명": file,
            "교과목명": subject_name,
            "수업개요": course_outline,
            "수업목표 및 내용": course_goal,
            "주차별 학습목표": " | ".join(weekly_goals)
        })

summary_df = pd.DataFrame(summary_data)
summary_df.to_csv("syllabus_extracted_summary.csv", index=False, encoding="utf-8-sig")
print("✅ syllabus_extracted_summary.csv 파일로 저장 완료!")
