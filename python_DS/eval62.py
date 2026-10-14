# `for name, score in students:` 형태로 각 tuple을 두 변수로 한 번에 받아 순회하세요.
students = [
    ("윤서", 85),
    ("지우", 92),
    ("민준", 65),
    ("서윤", 78),
    ("도윤", 95),
]
target = input()

# 목표 발견 플래그 변수
found = False

# for 문으로 순회하며 두 변수에 각각 저장
for name, score in students:
    
    # 목표값과 이름이 일치할 시 점수 출력
    if name == target:
        print(f"점수: {score}")
        found = True

# 플래그 비활성화일 시
if not found:
    print("학생 없음")  #  문자열 출력
    
    

# 피드백
# for name, score in students:

#     # 목표값과 이름이 일치할 시 점수 출력
#     if name == target:
#         print(f"점수: {score}")
#         break  # 발견 시 즉시 종료 → else 블록 건너뜀

# else:
#     # 플래그 없이 '미발견' 처리: break 없이 루프가 완료되면 실행
#     print("학생 없음")