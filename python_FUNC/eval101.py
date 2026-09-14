# 한 줄을 공백으로 나눕니다. 토큰이 2개면 기본 구분자("-"), 3개면 셋째 값이 구분자입니다.
parts = input().split()

# TODO: sep 에 기본값 "-" 를 가진 함수를 직접 정의(def)하고,
#   토큰 개수(2 또는 3)에 따라 인자를 생략/전달해 호출한 뒤 결과를 print 하세요.

# 1. def로 매개변수 세개 a, b, sep(기본값 "-")
def join_two(a, b, sep="-"):

    """문자열 a와 b를 구분자 sep으로 이은 값을 반환"""
    # 2. return으로 반환값 설정
    return a + sep + b

# 3. 토큰 개수를 판별하여 결과값 저장
if len(parts) == 2:
    result = join_two(parts[0], parts[1])
elif len(parts) == 3:
    result = join_two(parts[0], parts[1], parts[2])
else:
    result = "토큰 수 초과됨"

# 4. 결과 출력
print(result)


# 피드백
# 한 줄을 공백으로 나눕니다. 토큰이 2개면 기본 구분자("-"), 3개면 셋째 값이 구분자입니다.
parts = input().split()

# 1. def로 매개변수 세개 a, b, sep(기본값 "-")
def join_two(a, b, sep="-"):
    """문자열 a와 b를 구분자 sep으로 이은 값을 반환

    Args:
        a (str): 첫 번째 단어
        b (str): 두 번째 단어
        sep (str): 구분자 (기본값 "-")
    Returns:
        str: a + sep + b
    """
    # 2. return으로 반환값 설정
    return a + sep + b

# 3. 토큰 개수를 판별하여 구분자 결정 후 함수 호출
sep = parts[2] if len(parts) == 3 else "-"  # 토큰이 3개면 셋째 값, 아니면 기본값
if len(parts) >= 2:
    joined_word = join_two(parts[0], parts[1], sep)  # 변수명을 맥락에 맞게 수정
else:
    joined_word = "토큰 수 부족"

# 4. 결과 출력
print(joined_word)