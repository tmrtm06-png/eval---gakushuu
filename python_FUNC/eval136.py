# key=value 토큰을 dict 로 파싱합니다(값은 문자열). 예: "name=철수 age=20" → opts={"name":"철수","age":"20"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 1. 매개변수 name과 **options를 가지는 함수를 정의
def register(name, **options):
    """
    options 내 key와 value를 =로 엮어 사전순 리스트 작성(key를 기준으로 함)
    name: (','를 구분자로 한 options)를 반환 - options 내 요소가 하나인 경우 ',' 구분자 출석되지 않음
    """
    # 2. options의 요소를 key를 기준으로 사전순으로 정렬한다 - lambda로 정렬 기준 명시
    # - name: (','를 구분자로 한 리스트) 를 반환
    options_list = [f"{key}={value}" for key, value in sorted(options.items(), key=lambda kv: kv[0])]
    return f"{name}: {','.join(options_list)}"

# ↓ 호출부 (수정하지 마세요) — name 은 name 매개변수로, 나머지는 **options 로 모임
print(register(**opts))


# 피드백
# 1. 매개변수 name과 **options를 가지는 함수를 정의
def register(name: str, **options: str) -> str:
    """
    options 내 key와 value를 =로 엮어 사전순 리스트 작성(key를 기준으로 함)
    name: (','를 구분자로 한 options)를 반환 - options 내 요소가 하나인 경우 ',' 구분자 출력되지 않음
    """
    # 2. options의 요소를 key를 기준으로 사전순으로 정렬한다
    # - key= 인자 생략: items() 기본 정렬이 이미 키 사전순
    options_list = [f"{key}={value}" for key, value in sorted(options.items())]
    joined = ','.join(options_list)
    # 3. 추가 옵션이 없으면 후행 공백 없이 'name:' 반환
    return f"{name}: {joined}" if joined else f"{name}:"