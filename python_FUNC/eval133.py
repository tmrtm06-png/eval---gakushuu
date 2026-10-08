# key=value 토큰을 dict 로 파싱합니다(값은 문자열). 예: "a=hi b=hello" → opts={"a":"hi","b":"hello"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 1. **kwargs를 매개변수로 가지는 함수를 정의
def longest_value(**kwargs):
    """kwargs 안의 할당 단어(values) 중 가장 긴 단어를 반환한다"""

    # 2. kwargs를 순회하며 word를 구한 후, 길이 변수와 비교하며
    # 길이가 긴 변수를 발견하면 변수 갱신 - 이후 길이 변수 반환
    longest_word = ""  # 가장 긴 단어를 판별하기 위한 변수 초기화
    for word in kwargs.values():
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(longest_value(**opts))



# 피드백
# 2. max()와 key=len을 이용해 가장 긴 값을 한 번에 반환
# len() 재계산 없이 내장 함수가 효율적으로 비교를 처리함
# return max(kwargs.values(), key=len)
