# 정수 합 평균이라도 `:.1f` 로 포맷하면 "85.0" 처럼 소수점 표시.
d1_sets = [
    {"수학": 80, "영어": 75, "과학": 90},
    {"A": 80, "B": 90},
    {"X": 100, "Y": 50},
]
d2_sets = [
    {"영어": 88, "역사": 70, "과학": 80},
    {"B": 80, "C": 90},
    {},
]
t = int(input())
d1 = d1_sets[t]
d2 = d2_sets[t]

# 각 dict의 키를 합집합 후 사전순으로 정렬
all_keys = sorted(set(d1.keys()) | set(d2.keys()))

# dict 합집합 key 리스트를 순회하며 key가 dict 안에 있는지 확인
for key in all_keys:

    # key가 d1과 d2 양 쪽에 있는 경우 : 두 value의 평균 구함
    if key in d1 and key in d2:
        value = (d1[key] + d2[key]) / 2

    # key가 d1에만 있는 경우 그대로 저장
    elif key in d1:
        value = d1[key]

    # key가 d2에만 있는 경우
    else:
        value = d2[key]

    # 각 과목과 해당 점수를 출력 - 모든 값을 소수 첫째자리까지
    print(f"{key}: {value:.1f}")