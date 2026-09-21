# 슬라이싱 두 조각을 이어 붙이면 그대로 회전이다. 반복문 없이 한 줄로 끝낼 수 있다.
n = int(input())

# .split()으로 한 줄로 나눠 입력받는다
std_list = input().split()

# 슬라이싱 값을 입력받는다
slice_target = int(input())

# 슬라이싱 값 만큼 슬라이싱 후 이어붙인다
# - 이어붙인 리스트를 공백 구분하여 한 줄로 출력
print(' '.join(std_list[slice_target:] + std_list[:slice_target]))

# 피드백
# - names, rotate_k와 같은 역할이 명확히 드러나는 변수명 고려