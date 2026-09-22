# 슬라이싱은 인덱스 범위를 벗어나도 빈 리스트를 돌려주기 때문에 양 끝 경계도 그냥 처리할 수 있습니다.
n = int(input())

# 점수를 .split()으로 나눠 입력받는다
scores_list = input().split()

# 제외할 인덱스를 입력받는다
except_id = int(input())

# 제외 인덱스만큼 슬라이싱하고 이어붙인 후, 공백 구분하여 한 줄로 출력
f_slicing = scores_list[:except_id]
b_slicing = scores_list[except_id + 1:]

combine_slice = f_slicing + b_slicing

print(' '.join(combine_slice))


# 피드백
# - 변수 사용 x로 같략화, 변수명 명확히
# 제외할 인덱스를 입력받는다
# exclude_idx = int(input())

# 앞·뒤 슬라이스를 한 번에 이어붙여 출력 (중간 변수 생략으로 간결화)
# print(' '.join(scores_list[:exclude_idx] + scores_list[exclude_idx + 1:]))