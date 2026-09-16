# 입력을 정수 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# 여기에 함수 total(*nums) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)

# 1. 매개변수 *nums(여러 값을 가지는 튜플 형식)를 가지는 함수를 정의
def total(*nums):
    """한줄로 입력받은 nums안 모든 요소를 더한 값을 반환 | 인자가 없으면 자동으로 0 반환됨"""
    # 2. nums 안의 값 총합을 반환
    return sum(nums)

# ↓ 호출부 (수정하지 마세요) — 리스트를 * 로 풀어 total 에 전달
print(total(*nums))



# 피드백
# - docstring 항목 상세화

# 입력을 정수 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# 여기에 함수 total(*nums) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)

# 1. 매개변수 *nums(여러 값을 가지는 튜플 형식)를 가지는 함수를 정의
def total(*nums):
    """한줄로 입력받은 nums안 모든 요소를 더한 값을 반환 | 인자가 없으면 자동으로 0 반환됨

    Args:
        *nums (int): 가변 위치 매개변수 — 0개 이상의 정수
    Returns:
        int: 모든 인자의 합 (인자 없으면 0)
    Example:
        total(1, 2, 3) -> 6
    """
    # 2. nums 안의 값 총합을 반환
    return sum(nums)

# ↓ 호출부 (수정하지 마세요) — 리스트를 * 로 풀어 total 에 전달
print(total(*nums))