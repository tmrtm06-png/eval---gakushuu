# (-점수, 이름) tuple sort 로 점수 내림차순 + 이름 사전순.
data_sets = [
    [("Alice", 85), ("Bob", 92), ("Carol", 85), ("Dave", 95)],
    [("A", 80), ("B", 90), ("C", 70)],
    [("X", 50), ("Y", 60)],
]
t = int(input())
students = data_sets[t]

# 점수 내림차순, 이름 사전순으로 튜플 리스트로 변환
std_score = [(-score, name) for name, score in students]

# 점수 내림차순으로 자동 정렬(neg_score), 이름 사전순으로 자동 정렬됨
std_score.sort()

# 학생 이름과 해당 점수를 출력
# - 이름은 좌측으로 6칸, 점수는 우측으로 4칸 정렬시킨다
# - 점수 출력 시, 변수 앞 마이너스 부호 필요
for neg_score, std_name in std_score:
    print(f"{std_name:<6}{-neg_score:>4}")
    
    
# 피드백 - 변수를 역할명에 맞춰 수정한다