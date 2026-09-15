# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 레벨(1), 2개면 둘째 값(정수)이 레벨입니다.
parts = input().split()

# TODO: level 에 기본값 1 을 가진 함수를 직접 정의(def)하고,
#   토큰 개수에 따라 인자를 생략/전달(레벨은 정수 변환)해 호출한 뒤 결과를 print 하세요.

# 1. def로 매개변수 name, level(기본값 1) 두 개를 가지는 함수 정의
def build_tag(name, level=1):

    """name 앞에 태그('#' * level)을 이어붙여 반환"""
    # 2. 반환값 설정 - "#" * level + name 한 값을 반환한다
    return "#" * level + name

# 3. 토큰 수를 판별하여 결과값 저장
if len(parts) == 1:
    result = build_tag(parts[0])
elif len(parts) == 2:
    result = build_tag(parts[0], int(parts[1]))  # 토큰이 두 개일 시, level 부분을 정수로 변환
else:
    raise ValueError(f"예상치 못한 토큰 수: {len(parts)}")
# 4. 결과 출력
print(result)


# 피드백
# 한 줄을 공백으로 나눕니다. 토큰이 1개면 기본 레벨(1), 2개면 둘째 값(정수)이 레벨입니다.
parts = input().split()

# 1. def로 매개변수 name, level(기본값 1) 두 개를 가지는 함수 정의
def build_tag(name, level=1):
    """name 앞에 태그('#' * level)을 이어붙여 반환

    Args:
        name (str): 제목 문자열
        level (int): 레벨, 기본값 1
    Returns:
        str: '#' * level + name
    """
    # 2. 반환값 설정 - "#" * level + name 한 값을 반환한다
    return "#" * level + name

# 3. 토큰 수를 판별하여 결과 출력
if len(parts) == 1:
    print(build_tag(parts[0]))
elif len(parts) == 2:
    print(build_tag(parts[0], int(parts[1])))  # 토큰이 두 개일 시, level 부분을 정수로 변환
# 입력 형식이 보장되므로 else 분기 생략 (필요 시 ValueError 추가 가능)