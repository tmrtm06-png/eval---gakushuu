# 추적 변수 두 개를 두고 for 순회로 비교 + 갱신.
data_sets = [
    [("윤서", 85), ("지우", 92), ("민준", 65), ("서윤", 78), ("도윤", 95)],
    [("A", 70), ("B", 90), ("C", 80)],
    [("solo", 70)],
]
t = int(input())
students = data_sets[t]

# 최고점과 해당 학생 이름을 구하기 위한 변수 초기화

# top_name = ""
# top_score = 0

top_name, top_score = students[0]  # 피드백) 오류 발생을 위해 첫 번째 학생으로 초기화

# for문으로 언패킹 - name과 score 변수에 각각 저장
for name, score in students:

    # 최고점 변수와 현재 점수를 비교하며, 현재 점수가 보다 큰 경우 학생 이름과 점수 변수 갱신
    if score > top_score:
        top_score = score
        top_name = name

# f-string으로 최고점과 학생 이름 출력
print(f"{top_name}: {top_score}")