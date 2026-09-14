# 각 단계 결과를 변수에 담아 다음 단계에 넘기는 식으로 작성하면 명료합니다.
words = input().split()

# 1. 입력받은 단어 중 길이가 3 이상인 단어만 필터링하여 저장
lower_filtered = [word.lower() for word in words if len(word) >= 3]

# 2. 변환된 단어들을 사전순으로 정렬
lower_filtered.sort()

# 3. 상위 세 개의 단어만 저장
top3_words = lower_filtered[:3]  # 인덱스 슬라이싱으로 상위 세 단어만 잘라냄

# 4. 상위 세 개 단어를 공백 구분하여 한 줄로 출력
# - 아무것도 없을 시, 빈 줄이 출력됨
print(' '.join(top3_words))