# 정수 리스트 변환 후 두 번째 줄에서 a, b 를 받아 del 슬라이싱 한 줄로 처리하세요.
n = int(input())  # 현 문제에서는 사용하지 않는다

# .split()으로 한 줄로 나눠 입력받는다
nums = input().split()  # .join 출력용이므로 정수 변환 필요 X

# .split()으로 슬라이싱 범위 시작, 끝을 각각 입력받은 후
# map() 내장함수로 정수 변환
start_idx, end_idx = map(int, input().split())

# 두 인덱스 사이에 해당하는 요소를 한 번에 삭제
del nums[start_idx:end_idx]

# 공백 구분하여 한 줄로 출력 - 빈 리스트인 경우 빈 줄 출력됨
print(' '.join(nums))