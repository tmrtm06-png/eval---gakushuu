# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# TODO: 여기에 함수 average_args(*nums) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)

# 1. 매개변수 *nums를 가지는 함수를 정의
def average_args(*nums):
    """nums 내 숫자들의 평균을 반환 - 정수 나눗셈으로 소숫점 버림"""
    # 2. nums의 평균을 반환한다
    return sum(nums) // len(nums)

# ↓ 호출부 (수정하지 마세요)
print(average_args(*nums)) 


# 피드백
# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 1. 매개변수 *nums를 가지는 함수를 정의
def average_args(*nums: int) -> int:  # 타입 힌트 명시
    """nums 내 숫자들의 평균을 반환 - 정수 나눗셈으로 소숫점 버림"""
    # 2. nums의 평균을 반환한다
    return sum(nums) // len(nums)  # 타입 힌트 추가로 의도를 더 명확하게 표현

# ↓ 호출부 (수정하지 마세요)
print(average_args(*nums))