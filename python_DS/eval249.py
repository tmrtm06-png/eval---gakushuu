# while True 안에서 입력 받고 END 면 break. 새 입력은 append, 길이 > K 이면 `lst.pop(0)` 으로 가장 오래된 것 제거.
k = int(input())

# 문자열 입력 리스트
chr_list = []

# 무한 루프
while True:

    # 문자열을 입력받는다
    cmd = input()

    # END가 입력되었을 때, 반복문 종료
    if cmd == "END":
        break

    # - 이후 END가 아닐 경우 리스트에 이어붙인다
    chr_list.append(cmd)

    # 리스트 길이가 k를 초과할 경우 .pop(0)로 가장 오래된 값 제거
    if len(chr_list) > k :
        chr_list.pop(0)
    
# 리스트 내에 아무것도 없는 경우 공백 출력
# - 리스트 내 문자열이 있는 경우 최근 k개의 문자열을 공백 구분하여 한 줄로 출력
if not chr_list:
    print()
else:
    # 명령 개수만큼 슬라이싱 한 후, 공백 구분하여 한 줄로 출력
    print(' '.join(chr_list[-k:]))



# 피드백
from collections import deque

# while True 안에서 입력 받고 END 면 break. 새 입력은 append, maxlen으로 자동 관리.
k = int(input())

# 최근 K개만 자동으로 유지하는 덱 (maxlen 초과 시 가장 오래된 항목 자동 제거)
recent_cmds = deque(maxlen=k)  # deque(maxlen=k): pop(0) O(N) → O(1)

# 무한 루프
while True:

    # 문자열을 입력받는다
    cmd = input()

    # END가 입력되었을 때, 반복문 종료
    if cmd == "END":
        break

    # END가 아닐 경우 덱에 추가 (maxlen 초과 시 자동으로 가장 오래된 값 제거)
    recent_cmds.append(cmd)

# 리스트 내 문자열이 있으면 공백 구분, 없으면 빈 줄 출력
print(' '.join(recent_cmds))