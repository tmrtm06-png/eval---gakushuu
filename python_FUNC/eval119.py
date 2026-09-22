# 첫 토큰=배수(factor), 나머지=더할 정수들. 예: "2 1 2 3" → factor=2, nums=[1, 2, 3]
parts = input().split()
factor = int(parts[0])
nums = [int(x) for x in parts[1:]]

# 1. 매개변수 factor와 *nums를 가지는 함수를 정의
def sum_scaled(factor, *nums):
    """factor * sum(nums)를 반환. nums가 없으면 0 반환."""
    # 2. sum(nums)로 합산 후 factor를 곱해 반환 (nums가 빈 튜플이면 sum()은 0 반환)
    return factor * sum(nums)

# ↓ 호출부 (수정하지 마세요) — factor 는 위치 인자, 나머지는 * 로 풀어 전달
print(sum_scaled(factor, *nums))