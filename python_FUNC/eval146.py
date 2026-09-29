# 첫 토큰=제목, 나머지=정수 점수들. 예: "합계 1 2 3" → title="합계", values=[1, 2, 3]
parts = input().split()
title = parts[0]
values = [int(x) for x in parts[1:]]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def summary(title, *nums):
    s = 0
    for n in nums:
        s += n
    return title + ": " + str(s)

# title은 그대로, values 는 * 로 풀어 summary(title, *values) 를 호출하고 결과를 출력
print(summary(title, *values))