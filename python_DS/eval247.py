# 작성 코드
# 각 문서를 split 한 list 안에 검색어가 있는지 `in` 으로 검사.
docs = [
    "the cat sat on the mat",
    "the dog jumped over the cat",
    "python is fun",
    "i love programming",
    "the quick brown fox",
]
query = input()

# 검사 대상이 위치한 인덱스
sep = []

# docs 리스트를 순회하며 각 문장을 .split으로 공백 구분하여 분해
for i, sentence in enumerate(docs):
    words = sentence.split()
    
    # 검사 대상이 포함된 경우만 위치 인덱스에 저장
    if query in words:
        sep.append(str(i))  # 인덱스를 문자열로 변경

# 결과가 있는 경우 인덱스를 공백 구분하여 출력
# - 없는 경우 "없음"을 출력
if sep:
    print(' '.join(sep))
else:
    print("없음")


# 피드백
# 변수명을 역할명이 잘 드러나게 작성하기
# ex) matched_indices 등