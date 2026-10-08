# 입력을 정수 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def add3(a, b, c):
    return a + b + c

# 언패킹으로 리스트 인자를 풀어 add3에 전달한다
print(add3(*nums))