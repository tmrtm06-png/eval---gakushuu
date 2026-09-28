# 첫 토큰=기준값(threshold), 나머지=검사할 정수들. 예: "5 3 6 1 8" → threshold=5, nums=[3, 6, 1, 8]
parts = input().split()
threshold = int(parts[0])
nums = [int(x) for x in parts[1:]]

# 1. 매개변수 threshold와 *nums를 가지는 함수를 정의
def count_above(threshold, *nums):
    """*nums 내 threshold를 초과하는 값의 개수를 반환한다"""
    
    # 2. nums를 순회하며 각 요소를 threshold와 비교
    # - 초과값의 개수를 카운트하여 변수에 저장
    over_count = 0
    for num in nums:
        if num > threshold:
            over_count += 1
    
    return over_count

# ↓ 호출부 (수정하지 마세요) — threshold 는 위치 인자, 나머지는 * 로 풀어 전달
print(count_above(threshold, *nums))