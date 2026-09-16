# 빈도 dict 후 (-count, name) tuple 정렬 → 빈도 내림차순. 별은 `"*" * count`.
words = input().split()

# 비어있는 빈도 dict 작성
word_frequency = {}

# 입력받은 문자열을 순회
for word in words:

    # {단어: 빈도} 형태의 dict를 작성한다
    word_frequency[word] = word_frequency.get(word, 0) + 1

# 빈도를 기준으로 내림차순으로 정렬
# - (-빈도, 단어) 형태의 튜플로 저장됨
sorted_words = sorted([(-frequency, word) for word, frequency in word_frequency.items()])

# 튜플을 언패킹 후, 빈도 * "*"하여 막대 그래프 작성
# - 단어: (막대그래프) 형태로 출력한다
for neg_frequency, word in sorted_words:
    print(f"{word}: {-neg_frequency * '*'}")
    
    
# 피드백
# 빈도 dict 후 (-count, name) tuple 정렬 → 빈도 내림차순. 별은 `"*" * count`.
words = input().split()

# collections.Counter로 빈도 집계를 한 줄로 처리 (기존 for 루프와 동일한 결과)
from collections import Counter
word_frequency = Counter(words)  # {단어: 빈도} dict

# 빈도를 기준으로 내림차순으로 정렬
# - (-빈도, 단어) 형태의 튜플로 저장됨
# - Python의 안정 정렬 덕분에 빈도가 같은 단어는 입력 순서 유지
sorted_words = sorted([(-frequency, word) for word, frequency in word_frequency.items()])

# 튜플을 언패킹 후, 빈도 * "*"하여 막대 그래프 작성
# - 단어: (막대그래프) 형태로 출력한다
for neg_frequency, word in sorted_words:
    print(f"{word}: {-neg_frequency * '*'}")