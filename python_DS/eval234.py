# 빈도 dict 빌딩 후, 다시 enumerate 순회하며 counts[c]==1 인 첫 글자 위치 찾기.
s = input()

# 빈도 dict
char_count = {}

# 입력받은 문자열의 철자 빈도 dict를 작성
for char in s:
    char_count[char] = char_count.get(char, 0) + 1

# 한 번만 등장한 글자 중 가장 먼저 등장한 글자의 인덱스를 출력
# - enumerate로 인덱스와 글자 순회, 빈도 dict 조회 시 value가 1인 경우 출력 후 즉시 종료
for i, ch in enumerate(s):
    if char_count[ch] == 1:
        print(i)
        break
        
# - 모든 글자가 중복(1 초과)인 경우 -1을 출력
else:
    print(-1)
    
    
# 피드백
# 빈도 dict 빌딩 후, 다시 enumerate 순회하며 counts[c]==1 인 첫 글자 위치 찾기.
from collections import Counter  # Counter로 빈도 계산을 간결하게 처리

s = input()

# 빈도 dict
char_count = Counter(s)  # 기존 수동 루프와 동일한 결과, 코드 간결화

# 한 번만 등장한 글자 중 가장 먼저 등장한 글자의 인덱스를 출력
# - enumerate로 인덱스와 글자 순회, 빈도 dict 조회 시 value가 1인 경우 출력 후 즉시 종료
for i, char in enumerate(s):  # 변수명 ch -> char 로 통일
    if char_count[char] == 1:
        print(i)
        break

# - 모든 글자가 중복(1 초과)인 경우 -1을 출력
else:
    print(-1)