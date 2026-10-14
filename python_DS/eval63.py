# (점수, 이름) tuple 의 자연스러운 정렬을 활용하세요.
data_sets = [
    [(85, "윤서"), (92, "지우"), (65, "민준"), (78, "서윤"), (95, "도윤")],
    [(80, "A"), (70, "B"), (90, "C")],
    [(50, "혼자")],
]
t = int(input())
students = data_sets[t]

# 오름차순으로 정렬
# - sorted는 원본 리스트 수정 X - 새 리스트 반환
student_sorted = sorted(students)

# 결과 출력
for score, name in student_sorted: # 오름차순 tuple로 점수와 이름 반환
    print(f"{name}: {score}")    # 이름, 점수 순으로 출력