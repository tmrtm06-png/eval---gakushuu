# 1부터 N 사이의 해밍수를 출력하세요.
N = int(input())

# 해밍수 판단 기준의 소인수 리스트 작성 - (2, 3, 5)
hamming_num = [2, 3, 5]

# 입력받은 N의 범위만큼 반복
for i in range(1, N + 1):
    num = i  # 계산을 위해 i를 num으로 
    
    # 리스트 내 소인수를 각각 순회
    for p in hamming_num:
        # num을 해밍수로 나누어떨어질 때까지 반복
        while num % p == 0:
            num //= p  # p로 나눈 값을 갱신
    
    # 모든 해밍수 출력 위해 반복문 내에서 출력한다
    # - num이 1인 경우 i를 출력 - 해밍수가 출력됨
    if num == 1:
       print(i)
       
       
# 피드백
# 해밍수 판단 기준의 소인수 튜플 - 변경되지 않는 상수이므로 튜플 사용
HAMMING_FACTORS = (2, 3, 5)


def is_hamming(n: int) -> bool:
    """n이 해밍수인지 판별: 소인수가 2, 3, 5뿐이면 True"""
    for p in HAMMING_FACTORS:
        # 원본을 보존하고 소인수 분해용 복사본으로 나누기
        while n % p == 0:
            n //= p
    return n == 1  # 모두 나눈 후 1이면 해밍수


# 입력받은 N의 범위만큼 반복하며 해밍수 출력
for i in range(1, N + 1):
    if is_hamming(i):
        print(i)