# 작성 코드
# 한 번의 items() 순회로 합·최대·최소·합격수를 모두 누적 가능.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95, "예준": 50},
    {"A": 80, "B": 62, "C": 90, "D": 55},
    {"혼자": 100},
]
t = int(input())
scores = data_sets[t]

# 학생 전체 평균 구하기
std_average = sum(scores.values()) / len(scores)

# 최고점, 최저점 / 합격자, 합격률을 구하기 위한 변수 작성
top_std = ""
top_score = -1  
bot_std = ""
min_score = 101
pass_count = 0

# 학생: 점수 리스트를 .items()로 순회하여 각각 구함
for std, score in scores.items():

    # 최고점과 해당 학생을 갱신
    if score > top_score:
        top_score = score
        top_std = std

    # 최저점과 해당 학생을 갱신
    if score < min_score:
        min_score = score
        bot_std = std

    # 합격자 수 카운트
    if score >= 60:
        pass_count += 1

# 합격률 계산
pass_rate = (pass_count / len(scores)) * 100

# 각 결과를 한 줄씩 출력
# - 평균은 소수 첫째자리까지 구함
print(f"전체 평균: {std_average:.1f}")
print(f"최고점: {top_std} ({top_score})")
print(f"최저점: {bot_std} ({min_score})")
print(f"합격자: {pass_count}명")
print(f"합격률: {pass_rate:.1f}%")


# 피드백

# 최고점, 최저점 / 합·합격자를 구하기 위한 변수 작성
top_name = ""
top_score = float("-inf")  # 매직 넘버 대신 음의 무한대 사용 → 점수 범위에 무관하게 안전
bot_name = ""
min_score = float("inf")   # 양의 무한대로 초기화
total_score = 0
pass_count = 0

# 학생: 점수 리스트를 .items()로 순회하여 각각 구함
for student_name, score in scores.items():  # std → student_name: 표준 라이브러리 약어와 혼동 방지

    # 합산 (평균을 루프 안에서 처리해 values() 이중 순회 제거)
    total_score += score

    # 최고점과 해당 학생을 갱신
    if score > top_score:
        top_score = score
        top_name = student_name

    # 최저점과 해당 학생을 갱신
    if score < min_score:
        min_score = score
        bot_name = student_name

    # 합격자 수 카운트
    if score >= 60:
        pass_count += 1

# 학생 전체 평균 구하기
std_average = total_score / len(scores)

# 합격률 계산
pass_rate = (pass_count / len(scores)) * 100

# 각 결과를 한 줄씩 출력
# - 평균은 소수 첫째자리까지 구함
print(f"전체 평균: {std_average:.1f}")
print(f"최고점: {top_name} ({top_score})")
print(f"최저점: {bot_name} ({min_score})")
print(f"합격자: {pass_count}명")
print(f"합격률: {pass_rate:.1f}%")