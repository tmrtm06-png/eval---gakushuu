# 한 줄을 공백으로 나눕니다. 첫 토큰=n, 둘째 토큰(있으면)=start. 토큰 1개면 start 는 기본값 1. (정수)
parts = input().split()

# start 에 기본값 1 을 가진 함수를 직접 정의(def)하고,
# 토큰 개수에 따라 정수로 변환해 인자를 생략/전달한 뒤 결과를 print 하세요.

# 작성한 코드
# 1. def로 함수를 정의
def range_sum(n, start=1):

    # 2. start부터 n까지의 정수 범위를 반환
    return sum(range(start, n + 1))

# 3. 토큰 개수를 판별하여 결과값 수정
if len(parts) == 1:
    n = int(parts[0])
    result = range_sum(n)
else:
    n = int(parts[0])
    start = int(parts[1])
    result = range_sum(n, start)

# 4. 결과값 출력
print(result)


# 피드백
# 한 줄을 공백으로 나눕니다. 첫 토큰=n, 둘째 토큰(있으면)=start. 토큰 1개면 start 는 기본값 1. (정수)
parts = input().split()

# start 에 기본값 1 을 가진 함수를 직접 정의(def)하고,
# 토큰 개수에 따라 정수로 변환해 인자를 생략/전달한 뒤 결과를 print 하세요.


# 1. def로 함수를 정의
def range_sum(n, start=1):
    """start부터 n까지의 정수 합을 반환한다."""
    # 2. 등차수열 공식으로 O(1) 계산 (매우 큰 n에도 효율적)
    return (n - start + 1) * (start + n) // 2

# 3. 토큰 개수를 판별하여 결과값 출력
if len(parts) == 1:
    print(range_sum(int(parts[0])))          # start 생략 → 기본값 1 사용
else:
    print(range_sum(int(parts[0]), int(parts[1])))  # start 명시 전달