# 입력을 정수 리스트로 만듭니다. 예: "3 1 4" → nums=[3, 1, 4]
nums = [int(x) for x in input().split()]

# 1. 매개변수 *nums를 가지는 함수 max_all을 정의한다
def max_all(*nums):
    """한줄로 입력받은 숫자 중, 최댓값을 반환""" 
    # 2. nums에 저장된(튜플) 숫자들에서 가장 큰 값만을 반환 - max() 사용
    return max(nums)

# ↓ 호출부 (수정하지 마세요)
print(max_all(*nums))