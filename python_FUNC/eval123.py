# 첫 토큰=개수(k), 나머지=정수들. 예: "2 1 2 3 4" → k=2, nums=[1, 2, 3, 4]
parts = input().split()
k = int(parts[0])
nums = [int(x) for x in parts[1:]]

# 1. 매개변수 k와 nums를 가지는 함수를 정의
def top_k_sum(k, *nums):
    
    # 2. 내림차순으로 정리(reverse=True)후, 입력받은 k만큼 인덱스 슬라이싱 한 값의 총합을 반환
    list_sorted = sorted(nums, reverse=True)
    return sum(list_sorted[:k])

# ↓ 호출부 (수정하지 마세요) — k 는 위치 인자, 나머지는 * 로 풀어 전달
print(top_k_sum(k, *nums))



# 피드백
# 첫 토큰=개수(k), 나머지=정수들. 예: "2 1 2 3 4" → k=2, nums=[1, 2, 3, 4]
parts = input().split()
k = int(parts[0])
nums = [int(x) for x in parts[1:]]

# 1. 매개변수 k와 nums를 가지는 함수를 정의
def top_k_sum(k, *nums):
    # 2. 내림차순 정렬 후 앞 k개의 합을 반환 (중간 변수 없이 한 줄로 처리)
    return sum(sorted(nums, reverse=True)[:k])  # list_sorted 변수 생략으로 간결화

# ↓ 호출부 (수정하지 마세요) — k 는 위치 인자, 나머지는 * 로 풀어 전달
print(top_k_sum(k, *nums))