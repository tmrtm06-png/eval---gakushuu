# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 커트라인(60), 2개면 둘째 값이 커트라인입니다. (정수)
parts = input().split()

# 1. def로 매개변수 score, pass_line(기본값 60) 두 개를 가지는 함수를 정의
def check_pass(score, pass_line=60):

    """
    입력받은 score를 pass_line과 비교
     - 합격인 경우: "합격"
     - 불합격인 경우: "불합격" 을 반환
    """
    # 2. return으로 반환값 설정
    # - 점수와 커트라인 비교
    if score >= pass_line:
        return "합격"
    else:
        return "불합격"

# 3. 토큰 개수 판별 후 결과값 저장
# - 비교 연산 위해 정수로 변환
if len(parts) == 1:
    result = check_pass(int(parts[0]))
elif len(parts) == 2:
    result = check_pass(int(parts[0]) , int(parts[1]))
else:
    result = "토큰 범위 초과"

# 4. 결과 출력
print(result)


# 피드백
# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 커트라인(60), 2개면 둘째 값이 커트라인입니다. (정수)
parts = input().split()

# 1. def로 매개변수 score, pass_line(기본값 60) 두 개를 가지는 함수를 정의
def check_pass(score, pass_line=60):
    """
    입력받은 score를 pass_line과 비교
     - 합격인 경우: "합격"
     - 불합격인 경우: "불합격" 을 반환
    """
    # 2. return으로 반환값 설정
    # - 점수와 커트라인 비교
    if score >= pass_line:
        return "합격"
    else:
        return "불합격"

# 3. 토큰 개수 판별 후 결과값 저장
# - 비교 연산 위해 정수로 변환
if len(parts) == 1:
    result = check_pass(int(parts[0]))
elif len(parts) == 2:
    result = check_pass(int(parts[0]), int(parts[1]))
else:
    raise ValueError(f"예상치 못한 토큰 수: {len(parts)}")  # 명확한 예외 신호 제공

# 4. 결과 출력
print(result)