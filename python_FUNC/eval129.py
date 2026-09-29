# key=value 토큰을 dict 로 파싱합니다(값은 정수). 예: "a=3 b=7" → opts={"a":3,"b":7}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = int(v)

# 1. 매개변수 **kwargs를 가지는 함수를 정의
def max_value_key(**kwargs):
    """kwargs 안의 value 중 가장 큰 값을 가지는 key값을 반환한다"""
    # 2. 가장 큰 value를 가지는 key를 반환
    # - 최대 key와 value 변수를 초기화 후, .items로 dict를 순회하며 key와 value를 구한다
    # 이후 max_value와 value를 비교하며 value가 절대적으로 큰 경우 max_key와 max_value를 갱신
    max_key = ""
    max_value = float('-inf')    # 매우 작은 실수값으로 초기값 초기화
    for key, value in kwargs.items():
        if value > max_value:
            max_value = value
            max_key = key
    
    return max_key   # 최대값을 가지는 key를 반환

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(max_value_key(**opts))


# 피드백
# key, value 변수를 current_key, current_value 등으로 명확히 역할 구분
# 내장 max()함수 사용 시 간결화 가능 return max(kwargs, key=kwargs.get)