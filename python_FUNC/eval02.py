# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "3 5" → a=3, b=5
num1, num2 = [int(x) for x in input().split()]

# 위 설명에 따라 함수를 직접 정의하고(def), 호출한 결과를 출력(print)
# 설계 → def 로 정의 → return 으로 값 반환 → 함수 호출 → 결과를 print

# 1. def로 함수 정의
def add(num1, num2):
    
    """두 정수의 합을 반환"""
    # 2. return으로 반환값 설정
    return num1 + num2   # 두 수의 합을 반환

# 3. 결과 출력
print(add(num1, num2))