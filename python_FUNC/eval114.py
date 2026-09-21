# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 여기에 함수 count_even(*nums) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)

# 1. 매개변수 *nums를 가지는 함수를 정의
def count_even(*nums):
    """튜플로 저장되는 nums 내 요소들 중, 짝수인 요소의 개수를 반환한다"""
    # 2. 짝수의 개수 판별하여 반환
    even_num = 0
    for num in nums:
        if num % 2 == 0:
            even_num += 1
    return even_num

# ↓ 호출부 (수정하지 마세요)
print(count_even(*nums)) 


# 피드백
# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 여기에 함수 count_even(*nums) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)

# 1. 매개변수 *nums를 가지는 함수를 정의
def count_even(*nums):
    """튜플로 저장되는 nums 내 요소들 중, 짝수인 요소의 개수를 반환한다"""
    # 2. 짝수의 개수 판별하여 반환 — 제너레이터 표현식으로 간결하게 표현
    return sum(num % 2 == 0 for num in nums)  # True==1, False==0 으로 합산됨

# ↓ 호출부 (수정하지 마세요)
print(count_even(*nums))