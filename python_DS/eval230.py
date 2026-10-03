# 그룹→점수 list dict 빌딩 후, sorted(keys) 순회로 sum/len/max/min 계산.
n = int(input())

# 그룹: 점수 dict 작성
group_and_scores = {}

# 입력값 n만큼 반복하며 그룹과 점수를 한 줄로 입력받는다
for _ in range(n):
    group, score = input().split(',')
    score = int(score)
    
    # 그룹이 점수 dict에 없을 시, 빈 리스트 생성
    if group not in group_and_scores:
        group_and_scores[group] = []

    # 빈 리스트에 점수 추가
    group_and_scores[group].append(score)

# key를 사전순으로 정렬
# - group을 key로 점수를 변수에 저장 - A B C 순 리스트 형식으로 저장된다
for group_key in sorted(group_and_scores.keys()):
    scores = group_and_scores[group_key]

    # 평균점, 최고점, 최저점을 각각 구한다
    average = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)

    # A, B, C의 평균・최고・최저점을 한 줄에 각각 출력 - 평균은 소수 첫째자리까지
    print(f"{group_key}: 평균 {average:.1f}, 최고 {max_score}, 최저 {min_score}")