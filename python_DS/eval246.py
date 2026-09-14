# 모든 시나리오는 max ≠ min 보장 (정규화 분모 0 회피).
data_sets = [
    [60, 70, 80, 90, 100],
    [50, 75, 100],
    [80, 100],
]
t = int(input())
scores = data_sets[t]

# 리스트를 순회하며 점수를 각각 구함
for score in scores:

    # 정규화 식으로 정규화 점수와 그에 따른 등급 판별
    # - 정규화 등급
    # 90점 이상: A , # 80점 이상: B , # 70점 이상: C , 60점 이상: D , 60점 미만: F
    normalization = round((score - min(scores)) / (max(scores) - min(scores)) * 100)

    if normalization >= 90:
        grade = "A"
    elif normalization >= 80:
        grade = "B"
    elif normalization >= 70:
        grade = "C"
    elif normalization >= 60:
        grade = "D"
    else:
        grade = "F"
        
    # 원본 점수와 각 정규화 점수, 등급을 한 줄로 출력
    print(f"{score}: 정규화 {normalization}, 등급 {grade}")
    

# 피드백
# min/max를 루프 밖에서 한 번만 계산해 변수에 저장 (반복 호출 방지)
min_score = min(scores)
max_score = max(scores)

# 리스트를 순회하며 점수를 각각 구함
for score in scores:

    # 정규화 점수 계산
    norm_score = round((score - min_score) / (max_score - min_score) * 100)

    # 등급 판별
    # 90점 이상: A, 80점 이상: B, 70점 이상: C, 60점 이상: D, 60점 미만: F
    if norm_score >= 90:
        grade = "A"
    elif norm_score >= 80:
        grade = "B"
    elif norm_score >= 70:
        grade = "C"
    elif norm_score >= 60:
        grade = "D"
    else:
        grade = "F"

    # 원본 점수와 각 정규화 점수, 등급을 한 줄로 출력
    print(f"{score}: 정규화 {norm_score}, 등급 {grade}")