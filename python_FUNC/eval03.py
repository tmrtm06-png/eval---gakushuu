# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "10 2" → a=10, b=2
num1, num2 = [int(x) for x in input().split()]

# 위 설명에 따라 함수를 직접 정의하고(def), 호출한 결과를 출력(print)하세요.
# 설계 → def 로 정의 → return 으로 값 반환 → 함수 호출 → 결과를 print



# 1. def로 함수 정의
def bigger(num1, num2):

    """두 값 중 큰 값을 반환"""
    # 2. return으로 반환값 설정
    if num1 >= num2:     # a가 b이상인 경우
        return num1  # a를 반환
    else:
        return num2   # b를 반환

# 3. 결과 출력
print(bigger(num1, num2))