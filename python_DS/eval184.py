# (`w.lower()`, `w`) tuple 리스트로 sort → 첫 원소가 정렬 키. 결과는 원본 두 번째 원소만 추출.
words = input().split()

# 소문자로 변경되어 정렬된 단어와, 원본 단어를 저장하는 리스트 작성
# - (소문자 변경 단어, 원본 단어) 형식의 튜플로 저장됨
sorted_words = []

# 입력받은 문자열을 순회하며 단어를 각각 구함
for word in words:
    sorted_words.append((word.lower(), word))

# 리스트 내 단어를 사전순으로 정렬
sorted_words.sort()

# 정렬된 리스트 내 원본 단어를 한 줄로, 공백 구분하여 출력
result = [origin_word for _, origin_word in sorted_words]
print(' '.join(result))



# 피드백
# (`w.lower()`, `w`) tuple 리스트로 sort → 첫 원소가 정렬 키. 결과는 원본 두 번째 원소만 추출.
words = input().split()

# 소문자로 변경되어 정렬된 단어와, 원본 단어를 저장하는 리스트 작성
# - (소문자 변경 단어, 원본 단어) 형식의 튜플로 저장됨
# sorted_words → word_pairs: 정렬 전 튜플 리스트임을 변수명으로 명확히 표현
word_pairs = [(word.lower(), word) for word in words]  # for+append를 컴프리헨션으로 간결하게

# 리스트 내 단어를 사전순으로 정렬
word_pairs.sort()

# 정렬된 리스트 내 원본 단어를 한 줄로, 공백 구분하여 출력
result = [origin_word for _, origin_word in word_pairs]
print(' '.join(result))