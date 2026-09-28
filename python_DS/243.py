# csv 의 첫 토큰을 키로 빈도 dict 빌딩 → (-count, user) tuple 정렬 → 상위 3개.
n = int(input())

# 사용자: 건수 dict 작성
rental_top = {}

# 입력받은 값 만큼 반복하며 사용자, 건수를 .split()으로 나눠 입력받는다
for _ in range(n):

    user, counts = input().split(",")

    # 빈도 dict 작성
    rental_top[user] = rental_top.get(user, 0) + 1

# 빈도 dict 내림차순으로 정렬 - 이후 상위 세 명 슬라이싱
sorted_dict = sorted([(-count, user) for user, count in rental_top.items()])
top_3_std = sorted_dict[:3]

# 상위 3 dict 순회
# - 요구 형식 {사용자: 횟수}에 맞춰 출력
for neg_count, user in top_3_std:
    print(f"{user}: {-neg_count}회")
    
    

# 피드백
# - 역할을 한 눈에 나타내는 변수명으로 작성
# csv 의 첫 토큰을 키로 빈도 dict 빌딩 → (-count, user) tuple 정렬 → 상위 3개.
n = int(input())

# 사용자: 건수 dict 작성
rental_top = {}

# 입력받은 값 만큼 반복하며 사용자, 책 제목을 .split()으로 나눠 입력받는다
for _ in range(n):
    user, book = input().split(",")  # counts → book: 실제로 책 이름을 받는 변수이므로 의미에 맞게 수정

    # 빈도 dict 작성
    rental_top[user] = rental_top.get(user, 0) + 1

# 빈도 dict 내림차순으로 정렬 - 이후 상위 세 명 슬라이싱
sorted_users = sorted([(-count, user) for user, count in rental_top.items()])  # sorted_dict → sorted_users: 실제 타입(list)과 내용을 반영한 이름
top3_users = sorted_users[:3]  # top_3_std → top3_users: 더 직관적인 이름

# 상위 3 순회
# - 요구 형식 {사용자: 횟수}에 맞춰 출력
for neg_count, user in top3_users:
    print(f"{user}: {-neg_count}회")