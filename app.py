# 1. 추천 정도 리스트 생성
recommend_levels = ["상", "중", "하"]

# 2. 뮤지컬 추천 및 소개 리턴 함수
def get_musical_guide(musical_name, mood):
    # 조건문: 뮤지컬 이름과 취향에 따른 추천 정도와 소개글 매칭
    if musical_name == "프랑켄슈타인":
        intro = "19세기 유럽을 배경으로 신이 되려 했던 과학자 빅터와 피조물의 비극적인 운명을 그린 대작 뮤지컬입니다."
        if mood == "어두움":
            level = recommend_levels[0]  # '상'
            reason = "어둡고 비극적인 서사와 강렬한 넘버가 취향에 완벽하게 부합합니다."
        else:
            level = recommend_levels[2]  # '하'
            reason = "작품 전반의 분위기가 매우 무겁고 비극적이라 밝은 취향과는 거리가 멉니다."
            
    elif musical_name == "맘마미아":
        intro = "그리스의 아름다운 섬을 배경으로 그룹 ABBA의 히트곡들로 채워진 유쾌하고 따뜻한 뮤지컬입니다."
        if mood == "밝음":
            level = recommend_levels[0]  # '상'
            reason = "신나는 음악과 해피엔딩 스토리가 밝은 취향에 딱 맞습니다."
        else:
            level = recommend_levels[1]  # '중'
            reason = "밝은 분위기지만 명곡들이 많아 어두운 취향이어도 무난하게 즐길 수 있습니다."
            
    elif musical_name == "레베카":
        intro = "맨덜리 저택을 둘러싼 미스터리와 긴장감 넘치는 반전이 돋보이는 스릴러 로맨스 뮤지컬입니다."
        if mood == "어두움":
            level = recommend_levels[0]  # '상'
            reason = "미스터리하고 스산한 분위기가 어두운 취향을 저격합니다."
        else:
            level = recommend_levels[1]  # '중'
            reason = "스릴러 요소가 강하지만 화려한 무대 연출 덕분에 흥미롭게 볼 수 있습니다."
            
    else:
        level = recommend_levels[2]
        intro = "목록에 없는 뮤지컬입니다."
        reason = "선택 가능한 3개의 뮤지컬 중에서 다시 골라주세요."

    # 추천 정도, 소개글, 추천 이유를 리턴
    return level, intro, reason


# 3. 사용자 입력 받기
print("=== 🎭 뮤지컬 맞춤 추천 가이드 ===")
print("선택 가능 뮤지컬: [프랑켄슈타인 / 맘마미아 / 레베카]")
selected_musical = input("뮤지컬을 선택하세요: ").strip()
selected_mood = input("선호하는 분위기를 선택하세요 (밝음 / 어두움): ").strip()

# 함수 호출하여 결과 받기
rec_level, description, rec_reason = get_musical_guide(selected_musical, selected_mood)

# 결과 출력
print(f"\n[선택한 뮤지컬: {selected_musical}]")
print(f"▶ 추천 정도: {rec_level}")
print(f"▶ 작품 소개: {description}\n")


# 4. for문으로 순회하여 표 생성용 데이터(리스트 내 딕셔너리 형태)로 전환
raw_results = [
    ("추천 정도", rec_level),
    ("추천하는 이유", rec_reason)
]

table_data = []  # 표 생성을 위한 최종 데이터 리스트

for category, content in raw_results:
    # 표의 각 행(Row)이 될 딕셔너리 구조로 변환
    row = {"구분": category, "내용": content}
    table_data.append(row)

# 5. 변환된 표 생성용 데이터 확인 및 마크다운 표 형태로 출력
print("=== 📊 표 생성용 데이터 (Raw Data) ===")
print(table_data)

print("\n=== 📋 최종 출력 표 ===")
print("| 구분 | 내용 |")
print("| :--- | :--- |")
for row in table_data:
    print(f"| {row['구분']} | {row['내용']} |")
