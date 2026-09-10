# 첫 값=정수 n, 나머지=리스트 items. 예: "5 1 2" → n=5, items=[1, 2]
parts = input().split()
n = int(parts[0])
items = [int(x) for x in parts[1:]]

# 1. def로 함수 정의
def change_both(num, lst):
    """num에 100을 더하고(불변 객체이기에 원본 n은 변하지 않는다), lst에 0을 이어붙인다(리스트는 가변 객체이므로 원본 items 변경됨)"""
    # 2. num에 100을 더하고, lst에 0을 이어붙인다
    num = num + 100
    lst.append(0)

# 3. 함수 호출 후, n과 items를 두 줄로 출력한다
change_both(n, items)
print(n)
print(items)