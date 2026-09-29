# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "width=4 height=5" → opts={"width":4,"height":5}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# 1. 매개변수 width, height를 가지는 함수를 정의 - value로 사각형 넓이 구하기
def rectangle_kw(width, height):
    """가로(width)와 세로(height) 정수값을 받아 사각형의 넓이를 계산 후 반환"""
    # 2. 가로(width) * 세로(height)의 결과값을 반환
    return width * height

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(rectangle_kw(**opts))


# 피드백
# def rectangle_kw(width: int, height: int) -> int:  
# 타입 힌트 추가로 의도를 명확하게 표현