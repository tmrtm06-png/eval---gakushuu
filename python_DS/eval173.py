# 빈도 dict 구축 → 2회 이상만 추출 → (-count, name) tuple 정렬로 내림차순.
words = input().split()

# 빈도 dict 구축을 위한 빈 dict
word_frequency = {}

# 한 줄로 입력받은 단어를 순회
for word in words:

    if word == " ":  # word가 공백인 경우 건너뛴다
        continue
    # dict 안에 단어가 없는 경우 word를 추가하고, 횟수를 + 1 카운트한다
    word_frequency[word] = word_frequency.get(word, 0) + 1

# 빈도가 2회 이상인 단어와 그 횟수만 필터링
duplicates = sorted(
    [(-count, word) for word, count in word_frequency.items() if count >= 2]
)

# 2회 이상만 필터링 한 튜플을 순회하며, 단어와 빈도를 출력
# 빈도 리스트 유무 확인
if duplicates:
    for neg_frequency, word_key in duplicates:
        print(f"{word_key}: {-neg_frequency}")

# 상기 코드에 걸리지 않은 경우, "중복 없음" 출력
else:
    print("중복 없음")