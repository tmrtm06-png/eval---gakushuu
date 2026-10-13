# key=value 토큰을 dict 로 파싱합니다(값은 문자열). 예: "b=2 a=1" → opts={"b":"2","a":"1"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v


# 1. 매개변수 **kwargs를 가지는 함수를 정의
def merge_to_string(**kwargs):
    """
    kwargs의 key와 value를 =로 이은 사전순으로 정렬된 리스트를 작성
    이후 각 리스트를 ',' 로 구분하여 반환
    """
    # 2. kwargs 내 key와 value를 .items로 순회하여 각각 구한 후, 사전순으로 정렬된 리스트를 작성 - 리스트 컴프리헨션 사용
    # - 이후 작성 리스트 내 요소를 ','로 구분하여 반환한다 - .join() 사용
    kv_list = sorted([f"{key}={value}" for key, value in kwargs.items()])
    return ",".join(kv_list)

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(merge_to_string(**opts))


# 피드백 
# - 정렬 기준을 명시적으로 드러내기
# 2. kwargs 내 key 기준으로 정렬하여 'key=value' 토큰 리스트 생성
    # - key=lambda kv: kv[0] 으로 정렬 기준(키)을 명시적으로 표현
    # kv_list = [f"{key}={value}" for key, value in sorted(kwargs.items(), key=lambda kv: kv[0])]
    # return ",".join(kv_list)