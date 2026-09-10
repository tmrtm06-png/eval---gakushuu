# while saved < goal: 현재 상태 출력 → 동전 입력 → saved 누적
goal = int(input())
saved = 0

# 목표 금액 goal을 입력받고, 그 이후 동전 금액을 한 줄씩 입력받아 누적
# 반복마다 "현재 x원 / 목표: g 원" 출력, 그 다음 동전을 입력
# 누적 금액이 목표 금액 이상이 되면 마지막으로 현 상태 한번 더 출력
# "목표 달성! 총 x원을 모았습니다." 를 출력 

# 반복문 작성
while saved < goal:
    print(f"현재: {saved}원 / 목표: {goal}원")
    coin = int(input())
    saved += coin
    
print(f"현재: {saved}원 / 목표: {goal}원")

print(f"목표 달성! 총 {saved}원을 모았습니다.")