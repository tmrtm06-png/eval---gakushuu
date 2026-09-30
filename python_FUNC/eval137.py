# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "base=1000 ship=500" → opts={"base":1000,"ship":500}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# 1. 매개변수 base와 **fees를 가지는 함수를 정의
def invoice(base, **fees):
    """base에 fees의 value의 총합을 더한 값을 반환"""
    # 2. fees를 순회하며 총 value의 합을 구한다
    # - 이후 반목문 바깥에서 base + total_value를 반환
    total_value = 0
    for value in fees.values():
        total_value += value
    
    return base + total_value

# ↓ 호출부 (수정하지 마세요) — base 는 base 매개변수로, 나머지는 **fees 로 모임
print(invoice(**opts))


# 피드백
# - .values() 내장함수와 sum()을 사용하여 간결화