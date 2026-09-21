# 입력을 단어 리스트로 만듭니다. 예: "a b c" → words=["a", "b", "c"]
words = input().split()

# 1. 매개변수 *words를 가진 함수를 정의
def concat_words(*words):
    """
    words 내 문자열을 '-'로 연결하여 반환
    
    Args: 
        *words: 1개 이상의 문자열 (문자열이 한 개인 경우, 해당 문자열이 반환됨)
    Returns:
        str: '-'로 연결한 문자열 (문자열이 한 개인 경우 구분자 사용 X)
    """
    # 2. 문자열을 연결하여 반환한다
    return '-'.join(words)

# ↓ 호출부 (수정하지 마세요)
print(concat_words(*words))


# 피드백
# def concat_words(*words: str) -> str:  # 타입 힌트 추가로 의도를 더 명확히 전달