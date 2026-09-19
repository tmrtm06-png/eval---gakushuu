# 입력을 정수 리스트로 만듭니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
nums = [int(x) for x in input().split()]

# 1. 매개변수 *args를 가지는 함수를 정의
def product_all(*nums):
    
    """입력받은 nums 내 모든 요소들의 곱한 값을 반환"""
    # 2. 리스트를 순회하며 리스트의 요소를 모두 곱한 result를 반환
    result = 1
    for num in nums:
        result *= num
    
    return result 

# ↓ 호출부 (수정하지 마세요)
print(product_all(*nums))