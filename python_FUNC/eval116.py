# 입력을 정수 리스트로 만듭니다. 예: "3 1 4" → nums=[3, 1, 4]
nums = [int(x) for x in input().split()]

# 1. 매개변수 *nums를 가지는 함수를 정의
def range_span(*nums):
    """
    nums 내 숫자 중, (최댓값 - 최솟값)한 값을 반환한다
    
    Args:
        *nums: 정수 1개 이상의 가변 인자 (인자가 1개인 경우 0)
    Returns:
        int: 최댓값 - 최솟값 (모두 같은 숫자인 경우 0)
    """
    # 2. max(), min() 내장 함수를 사용하여 (최댓값 - 최솟값) 후 반환
    return max(nums) - min(nums)

# ↓ 호출부 (수정하지 마세요)
print(range_span(*nums))


# 피드백 - docstring 상세화
"""
    nums 내 숫자 중, (최댓값 - 최솟값)한 값을 반환한다

    Args:
        *nums: 정수 1개 이상의 가변 인자 (인자가 1개인 경우 0)
    Returns:
        int: 최댓값 - 최솟값 (모두 같은 숫자인 경우 0)
    Example:
        >>> range_span(5)      # 인자가 1개면 0
        0
        >>> range_span(3,1,4)  # 4 - 1 = 3
        3
"""