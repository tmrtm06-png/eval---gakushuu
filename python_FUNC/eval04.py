# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "4 5" → w=4, h=5
w, h = [int(x) for x in input().split()]

# 위 설명에 따라 함수를 직접 정의하고(def), 호출한 결과를 출력(print)하세요.
# 설계 → def 로 정의 → return 으로 값 반환 → 함수 호출 → 결과를 print

# 1. def로 함수 정의
def area(w, h):
    
    """두 값의 곱(직사각형 넓이)을 반환"""
    # 2. return으로 반환값 설정
    return w * h  # 가로 * 세로

# 3. 결과 출력
print(area(w, h))