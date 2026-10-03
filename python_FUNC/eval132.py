# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "a=5 b=-3" → opts={"a":5,"b":-3}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# 1. kwargs를 매개변수로 가지는 함수를 정의
def sum_positive_values(**kwargs):
    
    # 2. kwargs를 순회하며 value를 각각 구한 후, 해당 value가 양수인 경우 총합 변수에 가산
    # - 이후 반복문 바깥에서 총합 변수 반환
    pos_total = 0 
    for num in kwargs.values():
        if num > 0:
            pos_total += num
    
    return pos_total


# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(sum_positive_values(**opts))


# 피드백
# - sum()과 제너레이터 표현식으로 간결하게 표현
#   return sum(value for value in kwargs.values() if value > 0)  # 양수만 필터링해 합산