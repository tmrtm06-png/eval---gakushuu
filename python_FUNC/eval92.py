# 작성 코드
# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# TODO: 최솟값·최댓값·합·평균(//) 네 값을 함께 return 하는 함수를 직접 정의(def)하고,
#   반환값을 언패킹해 "최솟값 최댓값 합 평균" 형식으로 출력(print)하세요.

# 1. def로 함수 정의
def stats4(nums):
    
    """입력받은 값의 최솟값·최댓값·합·평균(정수 나눗셈)을 반환"""
    # 2. return으로 반환값 설정
    n_min = min(nums)
    n_max = max(nums)
    n_sum = sum(nums)
    n_avg = n_sum // len(nums)
    return (n_min, n_max, n_sum, n_avg)  # 괄호로 반환값이 튜플임을 명시

# 3. 함수 호출하여 각각 네가지 변수에 언패킹
# - 최솟값~평균 순
nums_min, nums_max, nums_sum, nums_avg = stats4(nums)
print(nums_min, nums_max, nums_sum, nums_avg)


# 피드백
# input().split() 의 각 칸을 정수로 바꿔 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 1. def로 함수 정의
def stats4(nums: list) -> tuple:
    """입력받은 값의 최솟값·최댓값·합·평균(정수 나눗셈)을 반환"""
    
    # 빈 리스트 방어 처리 추가
    if not nums:
        return None

    # 2. return으로 반환값 설정
    n_min = min(nums)
    n_max = max(nums)
    n_sum = sum(nums)
    n_avg = n_sum // len(nums)
    return (n_min, n_max, n_sum, n_avg)  # 괄호로 반환값이 튜플임을 명시

# 3. 함수 호출하여 각각 네가지 변수에 언패킹
# - 최솟값~평균 순
nums_min, nums_max, nums_sum, nums_avg = stats4(nums)
print(nums_min, nums_max, nums_sum, nums_avg)