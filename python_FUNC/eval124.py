# key=value 토큰을 dict 로 파싱합니다. 예: "name=철수 age=20" → opts={"name":"철수","age":"20"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# make_profile(name, age) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)

def make_profile(name, age):

    return f"{name}({age})"


# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(make_profile(**opts))