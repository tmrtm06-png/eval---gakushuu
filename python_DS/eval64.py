# zip 은 짧은 쪽 길이까지만 짝지어 줍니다.
names_sets = [
    ["A", "B", "C", "D", "E"],
    ["윤서", "지우", "민준"],
    ["solo"],
]
scores_sets = [
    [85, 92, 78],
    [85, 92, 65],
    [42],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

for name, score in zip(names, scores):   # zip으로 차례대로 튜플 반환 -> 각 변수에 저장
    print(f"{name}: {score}")  # scores의 길이에서 멈춤