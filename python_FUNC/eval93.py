# 첫 줄은 한계값 T, 둘째 줄은 공백으로 구분된 정수들입니다.
# 예: 첫 줄 "10", 둘째 줄 "3 4 5 6" → threshold=10, nums=[3, 4, 5, 6]
threshold = int(input())
nums = [int(x) for x in input().split()]

# 앞에서부터 누적합을 더하다가 누적합 > threshold 가 되는 즉시 그 인덱스를 return(조기 종료),
# 끝까지 안 넘으면 -1 을 return 하는 함수를 직접 정의(def)한 뒤, 호출 결과를 print 하세요.


# 1. def로 함수 정의
def first_exceed(nums, threshold):
    """기준값과 한 줄로 숫자를 입력받아, 숫자의 합이 처음으로 기준값을 넘는 인덱스를 반환"""
    # 2. nums를 순회하며 각각 수를 더한다
    # - 만약 총합이 기준값을 처음으로 넘는 경우의 인덱스를 반환
    # - 끝까지 더해도 기준값을 넘지 않는 경우 -1을 반환
    result = 0
    for i, num in enumerate(nums):
        result += num
        if result > threshold:
            return i
    
    return -1  # else문 불필요

# 3. 함수 호출 후 출력
print(first_exceed(nums, threshold))