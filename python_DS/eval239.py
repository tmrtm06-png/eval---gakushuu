# 빈도 dict 후 (-count, word) tuple 리스트로 정렬 → 빈도 내림차순, 동률 시 단어 사전순. N-1 인덱스 접근.
words = input().split()
n = int(input())

# 입력받은 각 단어들의 빈도 dict 작성
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# 빈도 dict를 내림차순으로 정렬
sorted_words = sorted([(-count, word) for word, count in word_count.items()])

# 전체 단어 가짓수와 n이 다른 경우(초과한 경우) "없음" 출력
if n > len(sorted_words):
    print("없음")
else:
    neg_count, word = sorted_words[n - 1]  # 인덱스 접근(0부터 시작하기에 -1로 원본 인덱스 접근)
    print(f"{word}: {-neg_count}")