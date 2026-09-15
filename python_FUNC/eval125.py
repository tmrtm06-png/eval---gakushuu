# key=value 토큰을 dict 로 파싱합니다. 예: "a=1 b=2" → opts={"a":"1","b":"2"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 여기에 함수 count_kwargs(**kwargs) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)

# 1. def로 함수 정의 - 매개변수 kwargs는 키워드 인자들을 딕셔너리로 모아 저장한다
def count_kwargs(**kwargs):
    """키워드 인자의 개수를 반환한다"""
    # 2. kwargs 딕셔너리의 키 개수를 반환
    return len(kwargs)

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(count_kwargs(**opts))  


# 피드백
# key=value 토큰을 dict 로 파싱합니다. 예: "a=1 b=2" → opts={"a":"1","b":"2"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 1. def로 함수 정의 - 매개변수 kwargs는 키워드 인자들을 딕셔너리로 모아 저장한다
def count_kwargs(**kwargs) -> int:  # 반환 타입 힌트 추가
    """키워드 인자의 개수를 반환한다"""
    # 2. kwargs 딕셔너리의 키 개수를 반환
    return len(kwargs)

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(count_kwargs(**opts))