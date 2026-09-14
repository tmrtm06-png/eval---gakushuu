# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 증가폭(1), 2개면 둘째 값이 증가폭입니다. (정수)
parts = input().split()

# step 에 기본값 1 을 가진 함수를 직접 정의(def)하고,
# 토큰 개수에 따라 정수로 변환해 인자를 생략/전달한 뒤 결과를 print 하세요.

# 작성한 코드
# 1. def로 매개변수 n과 step(기본값 1)을 가지는 함수를 정의
def increment(n, step=1):

    """입력받은 값 n에 step만큼 증가시켜 반환"""
    # 2. return으로 반환값 설정
    return n + step

# 3. 토큰 개수 판별하여 결과값 수정
# - 반드시 정수로 변환하여야 함
if len(parts) == 1:
    result = increment(int(parts[0]))
else:
    result = increment(int(parts[0]), int(parts[1]))

# 4. 결과 출력
print(result)


# 피드백(docstring 구체적으로 작성)
"""입력받은 값 n에 step만큼 증가시켜 반환

    Args:
        n (int): 기준 정수
        step (int): 증가폭, 기본값 1  # Args/Returns 명시로 문서화 품질 향상
    Returns:
        int: n + step
"""