# 모음 모음을 set 또는 문자열로 두고, 각 글자가 모음에 없으면만 결과에 추가.
s = input()

# 대소문자 모음 모임을 작성
vowels = "aeiouAEIOU"

# 리스트 컴프리헨션으로 입력받은 문자열을 순회하며 vowels에 없는 경우만 선별하여 저장
not_vowel = [char for char in s if char not in vowels]

# 한 줄로 출력 - 모두 모음인 경우 공백 출력됨
print(''.join(not_vowel))

# 피드백
# 대소문자 모음 집합을 set으로 선언 — in 검색이 O(1)로 더 효율적
vowels = set('aeiouAEIOU')

# 제너레이터 표현식으로 중간 리스트 없이 바로 join — 메모리 절약
result = ''.join(char for char in s if char not in vowels)

# 한 줄로 출력 - 모두 모음인 경우 빈 문자열이 출력됨
print(result)