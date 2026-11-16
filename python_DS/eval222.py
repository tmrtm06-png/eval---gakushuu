# 한 번 순회하며 `target - 현재값` 이 이미 dict 에 있으면 그 인덱스 + 현재 인덱스 출력. 아니면 현재값을 dict 에 등록.
nums = [int(x) for x in input().split()]
target = int(input())

# 0. 인덱스 추적 dict - 이미 확인한 값
seen = {}

# 1. enumerate로 인덱스와 각 숫자를 순회
for i, num in enumerate(nums):
    needed = target - num  # target을 구하기 위해 필요한 짝

    # 2. 필요한 값이 이미 dict 안에 있다면 각 쌍의 인덱스를 출력
    if needed in seen:
        print(seen[needed], i)
        break

    # 3. dict 내에 없다면 해당 값의 인덱스를 추가
    seen[num] = i

# 4. 조건을 만족하는 쌍이 없으면 "없음" 출력
else:
    print("없음")