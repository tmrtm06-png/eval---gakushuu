# 첫 줄: input().split() 으로 공백마다 잘라 문자열 리스트.  예: "a b c" → items == ["a", "b", "c"]
items = input().split()

# 둘째·셋째 줄: int(input()) 으로 정수 하나씩 읽기
k = int(input())
p = int(input())

# 입력받은 글을 최신순으로 정렬 - 역순
items.reverse()

# 페이지 슬라이싱 범위 - 시작과 끝 정함
# - p가 1인 경우 인덱스 0에서부터 시작, 2인 경우 3에서부터 시작
start = (p - 1) * k
end = start + k

# 인덱스 슬라이싱
sliced_items = items[start:end]

# 슬라이싱 리스트를 공백 구분하여 한 줄로 출력
# - 아무것도 없는 경우 "빈 페이지" 출력
if sliced_items:
    result = ' '.join(sliced_items)
else:
    result = "빈 페이지"

print(result)



# 피드백
# - page_size, page_num 등 의미있는 변수명으로 작성