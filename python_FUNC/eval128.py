# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "a=1 b=2" → opts={"a":1,"b":2}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# 1. 매개변수 **kwargs를 가지는 함수를 정의
def sum_values(**kwargs):
   
    # 2. kwargs(dict) 내 value 값의 총합을 반환
    return sum(kwargs.values())

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(sum_values(**opts))