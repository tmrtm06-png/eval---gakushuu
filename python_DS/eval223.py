# dict 로 빈도 카운트 후, 가장 많이 등장한 원소가 `len(nums) // 2` 보다 많이 등장하는지 검사.
nums = [int(x) for x in input().split()]

# 0. 빈도 dict 작성
num_frequency = {}
for num in nums:
    num_frequency[num] = num_frequency.get(num, 0) + 1

# 1. 절반 초과 등장하는 값 판별 위한 변수 작성
strictly_more_than = len(nums) // 2

# 2. 절반 초과로 등장하는 값을 출력
# - 없는 경우 "없음" 출력
for v, f in num_frequency.items():
    if f > strictly_more_than:
        print(v)
        break # 만족하는 값 발견 시 즉시 종료
else:
    print("없음")
    

# 피드백
# from collections import Counter  # 빈도 집계를 간결하게 처리
# 빈도 Counter 함수 사용으로 간결화
# strict~ → half_len 함수명을 명확한 이름으로 변경