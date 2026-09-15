# 빈도 dict 후 items 순회로 (count 가 strict 하게 클 때만 갱신) 첫 본 단어가 동률 시 유지됨.
words = input().split()

# 빈도 dict
word_frequency = {}

# 입력받은 단어를 순회하며 빈도 dict를 작성
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

# 최대 빈도의 단어와, 그 빈도를 구하기 위한 변수 작성
max_word = ""
max_count = 0

# 빈도 dict를 순회하며 단어와 횟수를 각각 구함
for key, count in word_frequency.items():
    # 최대 빈도와 단어당 빈도를 비교
    # 최대 빈도와 해당 단어 변수를 갱신
    if count > max_count:
        max_count = count
        max_word = key

# 해당 단어와 빈도를 한 줄로 출력
print(f"{max_word}: {max_count}")


# 피드백
# 빈도 dict 후 items 순회로 (count 가 strict 하게 클 때만 갱신) 첫 본 단어가 동률 시 유지됨.
words = input().split()

# 빈도 dict 초기화
word_frequency = {}

# 입력받은 단어를 순회하며 빈도 dict를 작성
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

# max()에 key 인자를 사용해 루프 없이 최빈 단어 탐색
# dict는 Python 3.7+ 에서 삽입 순서를 보장하므로 동률 시 첫 등장 단어가 선택됨
max_word = max(word_frequency, key=lambda w: word_frequency[w])
max_count = word_frequency[max_word]

# 해당 단어와 빈도를 한 줄로 출력
print(f"{max_word}: {max_count}")