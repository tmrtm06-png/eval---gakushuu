# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4 5" → nums=[1, 2, 3, 4, 5]
nums = [int(x) for x in input().split()]

# 1. 매개변수 *nums를 가지는 함수를 정의
def trimmed_sum(*nums):
    """nums 내 숫자의 전체 합에서 최댓값과 최솟값을 뺀 값을 반환"""
    # 2. nums의 전체 합 sum(nums)에서 최댓값과 최솟값을 제외한다
    return sum(nums) - min(nums) - max(nums)

# ↓ 호출부 (수정하지 마세요)
print(trimmed_sum(*nums))