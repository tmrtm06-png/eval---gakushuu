# chance = 3 로 시작, while chance > 0: 입력 → 비교 → 맞으면 break, 틀리면 chance -= 1
password = "python"
chance = 3

# 비밀번호를 입력받음
# 일치할 시 "로그인 성공!" 을 출력하고 종료
# 불일치 시 "틀렸습니다. 남은 기회{chance}번" 을 출력
# 세 번 모두 불일치 시, 마지막에 "계정이 잠겼습니다" 출력

# 반복문 작성
while chance > 0:
    user_input = input()
    if user_input == password:
        print("로그인 성공!")
        break
    else:
        chance -= 1
        if chance > 0:
            print("틀렸습니다. 남은 기회:", str(chance) + "번")
            
# break 없이 루프가 끝났다 -> 세 번의 시도 모두 실패
else:
    print("계정이 잠겼습니다")