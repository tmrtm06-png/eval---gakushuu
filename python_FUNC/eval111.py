# 입력을 정수 리스트로 만듭니다. 예: "3 1 4" → nums=[3, 1, 4]
nums = [int(x) for x in input().split()]

# 1. 매개변수 *nums를 가지는 함수를 정의
def min_all(*nums):
    """한줄로 입력받은 숫자들 중에서 가장 작은 값을 반환한다"""
    # 2. 튜플로 저장된 값 중 가장 작은 값을 반환 - min() 사용
    return min(nums)

# ↓ 호출부 (수정하지 마세요)
print(min_all(*nums))


# 피드백
# 입력을 정수 리스트로 만듭니다. 예: "3 1 4" → nums=[3, 1, 4]
nums = [int(x) for x in input().split()]

# 1. 매개변수 *nums를 가지는 함수를 정의
def min_all(*nums: int) -> int:  # 타입 힌트 추가로 함수 명세를 명확히 표현
    """한줄로 입력받은 숫자들 중에서 가장 작은 값을 반환한다.

    Args:
        *nums: 1개 이상의 정수
    Returns:
        가장 작은 정수 값
    """
    # 2. 튜플로 저장된 값 중 가장 작은 값을 반환 - min() 사용
    return min(nums)

# ↓ 호출부 (수정하지 마세요)
print(min_all(*nums))