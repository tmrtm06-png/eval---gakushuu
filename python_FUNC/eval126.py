# key=value 토큰을 dict 로 파싱합니다. 예: "b=2 a=1" → opts={"b":"2","a":"1"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 여기에 함수 list_keys(**kwargs) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
# 1. 매개변수 **kwargs를 가지는 함수를 정의 - dict 형식
def list_keys(**kwargs):

    # 2. kwargs의 key를 ","를 구분자로 한 줄로 반환
    # - 오름차순 정렬 필수
    return ",".join(sorted(kwargs.keys()))

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(list_keys(**opts))


# 피드백
# sorted(kwargs)는 dict 키를 순회하므로 .keys() 생략 가능
# return ",".join(sorted(kwargs))