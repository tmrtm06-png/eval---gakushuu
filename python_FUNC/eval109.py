# 입력을 정수 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# TODO: 여기에 함수 count_args(*args) 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)

# 1. def로 매개변수 args(튜플로 저장됨)을 가지는 함수를 정의
def count_args(*args):

    """arg에 저장된 요소의 총 개수를 반환한다"""
    # 2. args에 저장된 요소의 개수를 반환
    return len(args)

# ↓ 호출부 (수정하지 마세요)
print(count_args(*nums))