# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 1. 매개변수 nums를 가지는 함수를 정의
def first_and_last_sum(*nums):
    """입력받은 nums 내 인자들 중, 첫 인자와 마지막 인자의 합을 반환"""
    # 2. 인덱싱으로 첫 인자와 마지막 인자를 구함
    return nums[0] + nums[-1]

# ↓ 호출부 (수정하지 마세요)
print(first_and_last_sum(*nums))