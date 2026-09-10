# input() 으로 이름 한 줄을 읽습니다. 예: 입력이 "철수" 이면 name == "철수"
name = input()

# 위 설명에 따라 함수를 직접 정의하고(def), 호출한 결과를 출력(print)하세요.
# 설계 → def 로 정의 → return 으로 값 반환 → 함수 호출 → 결과를 print

# 1. def로 함수 정의, 함수명(입력값)
def greet(name):

    # 2. return으로 반환값 설정
    return f"안녕하세요, {name}님!"

# 3. 결과 출력 
print(greet(name))