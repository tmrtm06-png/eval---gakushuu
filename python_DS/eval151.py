# 빈도 dict 구축 → (-count, name) tuple 리스트로 정렬하면 빈도 내림차순으로 한 번에 정렬
words = input().split()

# 단어 빈도 dict 구축
counts = {}

# 입력받은 단어를 하나씩 순회하며 카운트
for w in words:
    counts[w] = counts.get(w, 0) + 1  # 첫 단어는 0이 기본값, 이후 +1 카운트

# 횟수 내림차순으로 정렬된 tuple 작성
count_sorted = sorted([(-count, word) for word, count in counts.items()])

# 상위 횟수 단어 세 개를 슬라이싱
result = [word for cnt, word in count_sorted[:3]]

# 공백으로 구분하여 한 줄로 출력
print(' '.join(result))