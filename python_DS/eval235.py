# split() 후 list 슬라이싱 [::-1] 또는 reverse() 메서드로 뒤집고 join.
words = input().split() # 입력받은 문자열을 공백으로 나눠 리스트 형태로 저장

# 저장된 문자열의 리스트를 뒤집는다
reversed_words = words[::-1]

# 뒤집어진 문자열을 공백 구분하여 한 줄로 출력
print(' '.join(reversed_words))