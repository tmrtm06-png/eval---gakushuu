# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 할인율(10), 2개면 둘째 값이 할인율(%)입니다. (정수)
parts = input().split()

# TODO: rate 에 기본값 10 을 가진 함수를 직접 정의(def)하고,
#   토큰 개수에 따라 정수로 변환해 인자를 생략/전달한 뒤 결과를 print 하세요.

# 1. def로 매개변수 price와 rate(기본값 10) 두 개를 가지는 함수 정의
def discount_price(price, rate=10):

    """원본 price에서 할인가를 뺀 값을 반환"""
    # 2. 할인 금액을 구한 후, 원본 가격에서 뺀 값을 반환
    dis_amount = price * rate // 100
    return price - dis_amount

# 3. 토큰 수를 판별한 후 결과값 저장
if len(parts) == 1:
    result = discount_price(int(parts[0]))
elif len(parts) == 2:
    result = discount_price(int(parts[0]), int(parts[1]))
else:
    raise ValueError(f"예상치 못한 토큰 수: {len(parts)}")  # 예외 신호 제공

# 4. 결과를 출력
print(result)