# `endswith` 와 슬라이싱 `w[:-3]`, `w[:-2]` 로 접미사 제거. 길이 조건 확인 필수.
words = input().split()

# 결과 출력을 위한 리스트
suffix_result = []

# 반복문으로 각각 순회하며 한 줄로 입력받은 문자열이 특정 접미사(ing, ed)로 끝나는지
# 문자의 길이를 판단 - word.endswith() 사용
# - 접미사가 존재하지 않는 경우에는 그대로 결과 리스트에 저장
for word in words:
    if word.endswith("ing") and len(word) >= 4:  # 문자열의 길이가 4 이상이고 "ing"로 끝나는 경우 접미사 제거
        suffix_result.append(word[:-3])
    elif word.endswith("ed") and len(word) >= 3:  # 문자열의 길이가 3 이상이고 "ed"로 끝나는 경우 접미사 제거
        suffix_result.append(word[:-2])
    else:
        suffix_result.append(word)

# 결과 리스트를 공백 구분하여 한 줄로 출력
print(' '.join(suffix_result))



# 피드백
# `endswith` 와 슬라이싱 `w[:-3]`, `w[:-2]` 로 접미사 제거. 길이 조건 확인 필수.
words = input().split()

# 결과 출력을 위한 리스트
# 리스트 컴프리헨션으로 간결하게 표현
suffix_result = [
    word[:-3] if word.endswith("ing") and len(word) >= 4  # 길이 4 이상 + ing 제거
    else word[:-2] if word.endswith("ed") and len(word) >= 3  # 길이 3 이상 + ed 제거
    else word  # 조건에 해당하지 않는 경우 그대로 유지
    for word in words
]

# 결과 리스트를 공백 구분하여 한 줄로 출력
print(' '.join(suffix_result))