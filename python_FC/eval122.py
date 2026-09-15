# 1!부터 N!까지 출력하고 합을 구하세요.
n = int(input())

# 총합 변수 초기화
total = 0 

# 팩토리얼 계산 변수 설정
result = 1

# 팩토리얼 간격 저장을 위한 공백 리스트
factor_term = []

# 반복문 범위 설정
for factor in range(1, n + 1):

    # 팩토리얼 계산, 총합 변수에 계산된 팩토리얼 더함
    result *= factor
    total += result
    
    # 리스트에 팩토리얼 하나씩 이어붙임
    factor_term.append(f"{factor}!")

    # 팩토리얼 형식에 맞게 출력
    print(f"{factor}! = {result}")

# 저장된 팩토리얼 간격 요소를 + 구분으로, 팩토리얼의 총합을 출력
print(" + ".join(map(str, factor_term)), "=", total)

# f-string 사용
# print(f"{ ' + '.join(factor_term)} = {total}")