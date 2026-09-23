# 첫 토큰=카테고리, 나머지=항목들. 예: "선호도 사과 바나나" → category="선호도", names=["사과","바나나"]
raw = input().split()
category = raw[0]
names = raw[1:]

# 1. 매개변수 category와 *names를 가지는 함수를 정의
def ranking(category, *names):
    """{category}: {' > '.join(names)} 형태로 구분하여 한 줄로 반환"""
    # 2. 입력받은 항목 순서대로 " > "로 구분하여 반환한다
    return f"{category}: {' > '.join(names)}"

# ↓ 호출부 (수정하지 마세요)
print(ranking(category, *names))

# 피드백
# - docstring, 입 출력 타입 명시
# 1. 매개변수 category와 *names를 가지는 함수를 정의
def ranking(category: str, *names: str) -> str:
    """
    category와 names를 받아 '{category}: 항목1 > 항목2 > ...' 형태의 문자열을 반환한다.
    """