# 입력을 정수 리스트로 만듭니다. 예: "1 -2 3" → nums=[1, -2, 3]
nums = [int(x) for x in input().split()]

# TODO: 여기에 함수 sum_positive(*nums) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)

# 1. 매개변수 *nums를 가진 함수를 정의
def sum_positive(*nums):
    """nums 내 양수의 값만을 더하여 반환한다"""
    # 2. 양수를 판별하여 총합값 변수에 더한 후 반환
    pos_total = 0
    for num in nums:
        if num > 0:
            pos_total += num
    return pos_total

# ↓ 호출부 (수정하지 마세요)
print(sum_positive(*nums))


# 피드백
# 입력을 정수 리스트로 만듭니다. 예: "1 -2 3" → nums=[1, -2, 3]
nums = [int(x) for x in input().split()]

# 1. 매개변수 *nums를 가진 함수를 정의
def sum_positive(*nums: int) -> int:
    """nums 내 양수의 값만을 더하여 반환한다

    Args:
        *nums (int): 임의 개수의 정수
    Returns:
        int: 양수들의 합 (양수가 없으면 0)
    """
    # 2. 제너레이터 표현식으로 양수만 필터링하여 합산 반환
    return sum(n for n in nums if n > 0)  # 양수(n > 0)만 합산, 0과 음수 제외

# ↓ 호출부 (수정하지 마세요)
print(sum_positive(*nums))