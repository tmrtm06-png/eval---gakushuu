# f-string `:+.1f` 로 부호 포함 소수점 포맷. 등수는 자신보다 큰 점수 수 + 1.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 조회 학생이 dict 내에 있는지 판별
if name in scores:

    # 조회 학생의 점수를 변수에 저장
    query_score = scores[name]

    # 작성된 {학생: 점수} dict의 점수 평균을 구한다
    score_average = sum(scores.values()) / len(scores)

    # 입력받은 학생의 점수와 평균 차이를 구한다
    # 학생 이름으로 dict 참조하여 점수 조회, 이후 평균 - 점수
    avg_score_diff = query_score - score_average
    
    # 조회 학생의 등수 구하기
    # dict 내 비교 점수가 조회 대상 점수 초과한 경우 등수 +1 - 등수는 1부터 시작하므로 sum 바깥에서 +1
    rank = sum(1 for s in scores.values() if query_score < s) + 1

    # 결과 출력은 하나의 블록 안에서 일괄 출력
    print(f"이름: {name}")
    print(f"점수: {query_score}")
    print(f"평균 차이: {avg_score_diff:+.1f}")  # f-string의 기능 변수:+로 부호 항시 표기, .1f로 소수 첫째자리까지 구함
    print(f"등수: {rank}등")

 # 학생이 없는 경우 "학생 없음" 출력   
else:
    print("학생 없음")