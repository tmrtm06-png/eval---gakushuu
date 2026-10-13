# key=value 토큰을 dict 로 파싱합니다. 예: "greeting=안녕 name=철수" → opts={"greeting":"안녕","name":"철수"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def greet(greeting, name):
    return greeting + ", " + name + "!"

# opts 를 **로 언패킹하여 greet 에 넘기고, 그 반환값을 출력한다
print(greet(**opts))


# 피드백 
# k, v = token.split("=", 1)  # maxsplit=1: 값에 '='이 포함되어도 안전하게 파싱