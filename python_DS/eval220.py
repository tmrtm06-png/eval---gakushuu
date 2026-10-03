# 소문자 변환 + split → 불용어 not in 필터 → 빈도 dict → (-count, word) tuple 정렬 → 상위 3개.
stopwords = {"a", "an", "the", "is", "are", "in", "on", "at", "and", "or", "but"}
text = input()

# 입력받은 텍스트를 소문자로 변환, .split()으로 나눠 저장
converted_text = text.lower().split()

# 불용어(stopwords) 목록에 없는 단어의 빈도 dict를 작성
filtered_dict = {}
for word in converted_text:
    if word not in stopwords:
        filtered_dict[word] = filtered_dict.get(word, 0) + 1

# 내림차순으로 빈도 dict를 정렬 - 상위 세 단어를 선별
word_count_top3 = sorted([(-count, word) for word, count in filtered_dict.items()])[:3]

# 상위 3개 dict를 "단어: 횟수" 형식으로 한 줄씩 출력
for neg_count, word in word_count_top3:
    print(f"{word}: {-neg_count}")