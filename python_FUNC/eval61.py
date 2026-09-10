# key=value 토큰을 dict 로 읽습니다(값은 정수). 예: "a=100 b=200" → prices={"a":100,"b":200}
prices = {}
for t in input().split():
    k, v = t.split("=")
    prices[k] = int(v)

# prices 의 모든 값을 10 줄이는 discount_all(d) 를 정의하고, 아래 줄 앞에서 discount_all(prices) 를 호출하세요.
# 1. def로 함수 정의
def discount_all(d):
    """d의 모든 할당값을 10씩 감소시킨다"""
    # 2. 함수 내에서 d를 순회하며 그 할당값에서 -10
    for key in d:
        d[key] -= 10

# 3. 함수 호출
discount_all(prices)

# ↓ 출력부 (제공됨) — 호출 후 바뀐 prices 를 키 사전순으로 출력
items = []
for k in sorted(prices):
    items.append(k + "=" + str(prices[k]))
print(",".join(items))