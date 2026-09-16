# 한 줄을 공백으로 나눕니다. 토큰 1/2/3 개에 따라 low, high 가 기본값으로 채워집니다. (모두 정수)
parts = input().split()

# low=0, high=100 기본값을 가진 함수를 직접 정의(def)하고,
# 토큰 개수(1/2/3)에 따라 정수로 변환해 인자를 생략/전달한 뒤 결과를 print 하세요.

# 1. def로 매개변수 세개 value, low(기본값 0), high(기본값 100)를 가지는
def clamp(value, low=0, high=100):
    
    """
    value와 low, high의 값을 입력받아, (low, high)의 범위 내에서 제한한 값을 반환
     - value < low인 경우 low를 반환
     - value > high인 경우 high를 반환
     - 그 사이인 경우 value 자신을 반환
    """
    # 2. value와 low, high의 값을 비교하며 반환값을 설정
    if value < low:
        return low
    elif value > high:
        return high
    else:
        return value

# 3. 토큰 수를 판별하여 결과값 수정
if len(parts) == 1:
    result = clamp(int(parts[0]))
elif len(parts) == 2:
    result = clamp(int(parts[0]), int(parts[1]))
else:
    result = clamp(int(parts[0]), int(parts[1]), int(parts[2]))
# parts의 개수가 1~3까지의 범위로 보장되어 있으므로, 방어 코드 불필요하다고 판단

# 4. 결과 출력
print(result)