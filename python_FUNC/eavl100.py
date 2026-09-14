# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 수량(1), 2개면 둘째 값이 수량입니다. (정수)
parts = input().split()

# TODO: count 에 기본값 1 을 가진 함수를 직접 정의(def)하고,
#   토큰 개수에 따라 정수로 변환해 인자를 생략/전달한 뒤 결과를 print 하세요.

# 1. def로 매개변수 unit_price와 count(기본값 1) 두 개를 가지는 함수를 정의
def total_price(unit_price, count=1):    

    """총액을 계산하여 반환"""
    # 2. unit_price * count 한 값을 반환
    return unit_price * count

# 3. 토큰 수를 판별하여 함수 호출 후 결과값 저정
# - 정수로 변경 필수
if len(parts) == 1:
    result = total_price(int(parts[0]))
else:
    result = total_price(int(parts[0]), int(parts[1]))

# 4. 결과 출력
print(result)


# 피드백
# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 수량(1), 2개면 둘째 값이 수량입니다. (정수)
parts = input().split()

# 1. def로 매개변수 unit_price와 count(기본값 1) 두 개를 가지는 함수를 정의
def total_price(unit_price, count=1):
    """총액을 계산하여 반환"""
    # 2. unit_price * count 한 값을 반환
    return unit_price * count

# 3. 토큰 수를 판별하여 함수 호출 후 결과값 저장
# - 정수로 변경 필수
if len(parts) == 1:
    result = total_price(int(parts[0]))
elif len(parts) == 2:  # 명시적 조건으로 예상치 못한 입력과 구분
    result = total_price(int(parts[0]), int(parts[1]))
else:
    raise ValueError(f"입력 토큰이 너무 많습니다: {parts}")

# 4. 결과 출력
print(result)