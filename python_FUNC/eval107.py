# 한 줄을 공백으로 나눕니다. 토큰 1/2/3 개에 따라 tax, ship 이 기본값으로 채워집니다. (모두 정수)
parts = input().split()

# 1. 세 개의 매개변수 base, tax(기본값 10), ship(기본값 0)를 가지는 함수를 정의
def price_with_options(base, tax=10, ship=0):
    """
    옵션별 결제 금액을 반환
     - 세금은 정수 나눗셈
    """
    # 2. 결제 금액을 반환한다
    return base + base * tax // 100 + ship

# 3. 토큰 개수 판별 후 결과값 산출
if len(parts) == 1:
    result = price_with_options(int(parts[0]))
elif len(parts) == 2:
    result = price_with_options(int(parts[0]), int(parts[1]))
else:
    result = price_with_options(int(parts[0]), int(parts[1]), int(parts[2]))
# parts의 개수가 1~3까지의 범위로 보장되어 있으므로, 방어 코드 불필요하다고 판단

# 4. 결과 출력
print(result)