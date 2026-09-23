# 첫 토큰=라벨(label), 나머지=점수들. 예: "수학 90 80 70" → label="수학", scores=[90, 80, 70]
parts = input().split()
label = parts[0]
scores = [int(x) for x in parts[1:]]

# 여기에 함수 report(label, *scores) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
# 1. 매개변수 label과 *scores를 가지는 함수를 정의
def report(label, *scores):
    """ {label}: {scores의 합} 의 형태로 반환"""

    # 2. sum()으로 scores의 총합을 구하여 반환 - scores의 요소가 하나인 경우 그 요소가 총합이 됨
    return f"{label}: {sum(scores)}"

# ↓ 호출부 (수정하지 마세요) — label 은 위치 인자, 나머지는 * 로 풀어 전달
print(report(label, *scores))


# 피드백
# - 매개변수 항목에 타입 힌트 추가
# 첫 토큰=라벨(label), 나머지=점수들. 예: "수학 90 80 70" → label="수학", scores=[90, 80, 70]
parts = input().split()
label = parts[0]
scores = [int(x) for x in parts[1:]]

# 여기에 함수 report(label, *scores) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)
# 1. 매개변수 label과 *scores를 가지는 함수를 정의
def report(label: str, *scores: int) -> str:  # 타입 힌트 추가로 명세를 명확히
    """라벨과 점수들을 받아 '{label}: {합계}' 형태의 문자열을 반환.

    Args:
        label (str): 출력할 라벨
        *scores (int): 0개 이상의 점수
    Returns:
        str: '{label}: {합계}' 형식 문자열
    """
    # 2. sum()으로 scores의 총합을 구하여 반환 - scores의 요소가 하나인 경우 그 요소가 총합이 됨
    return f"{label}: {sum(scores)}"

# ↓ 호출부 (수정하지 마세요) — label 은 위치 인자, 나머지는 * 로 풀어 전달
print(report(label, *scores))