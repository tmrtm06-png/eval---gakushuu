# 각 문자에 대해 `c.lower() in "aeiou"`, `c.isalpha()`, `c.isdigit()` 같은 메서드로 분기.
s = input()

# 자음, 모음, 숫자의 등장 횟수를 구하기 위한 변수 초기화
vowel = 0
consonant = 0
digit = 0

# 입력받은 문자열을 각각 순회하며 스펠링을 각각 구함
# - 공백, 기호는 무시한다
for char in s:
    
    # char가 숫자인 경우 숫자 변수 카운트 + 1
    if char.isdigit():
        digit += 1
    elif char.isalpha():  # 알파벳인지 판별

        # 해당 스펠링이 모음인 경우, 모음 변수에 카운트 + 1
        if char.lower() in "aeiou":
            vowel += 1
        else:   # 모음을 제외한 모든 영문 알파벳은 자음
            consonant += 1

# 모음, 자음 숫자 순서대로 각각 한 줄, 총 세 줄로 출력
print(f"모음: {vowel}")
print(f"자음: {consonant}")
print(f"숫자: {digit}")


# 피드백
# 모음을 상수 변수로 분리하여 저장한다
# ex_ VOWELS = "aeiou"