# # 메뉴→매출 dict 빌딩 후 `sorted(keys)` 순회로 출력.
# menu = {"커피": 4000, "라떼": 5000, "차": 3000, "케이크": 6000}
# n = int(input())

# # 주문받은 메뉴와 그 빈도 dict를 구축
# ordered_menu = {}

# # 입력받은 값 만큼 반복하며 주문을 입력받음
# for _ in range(n):
#     order = input()
    
#     # {메뉴: 개수} 식의 dict 작성, 주문이 없는 경우 0, 있는 경우 +1 가산
#     ordered_menu[order] = ordered_menu.get(order, 0) + 1
    
# # 상단 메뉴를 참조하여 매출 dict 작성
# sales_menu = {}

# # 주문 dict를 순회하며 가격표 dict의 가격 참조하여 매출 계산
# for item, count in ordered_menu.items():
#     sales_menu[item] = count * menu[item]

# # 매출 dict를 순회하며, 메뉴명 사전순으로 메뉴와 해당 매출을 출력
# # - 아무것도 주문하지 않은 경우 빈 줄 출력됨
# for menu_name in sorted(sales_menu.keys()):
#     print(f"{menu_name}: {sales_menu[menu_name]}원")
    
# 피드백
# 메뉴→매출 dict 빌딩 후 `sorted(keys)` 순회로 출력.
menu = {"커피": 4000, "라떼": 5000, "차": 3000, "케이크": 6000}
n = int(input())

# 주문받은 메뉴와 그 빈도 dict를 구축
ordered_menu = {}

# 입력받은 값 만큼 반복하며 주문을 입력받음
for _ in range(n):
    order = input()

    # {메뉴: 개수} 식의 dict 작성, 주문이 없는 경우 0, 있는 경우 +1 가산
    ordered_menu[order] = ordered_menu.get(order, 0) + 1

# 상단 메뉴를 참조하여 매출 dict 작성
# ordered_menu와 통합: 바로 매출 누적도 가능하나 가독성을 위해 분리 유지
sales_menu = {
    item: count * menu[item]  # 주문 횟수 × 단가 → 총 매출
    for item, count in ordered_menu.items()
}

# 매출 dict를 순회하며, 메뉴명 사전순으로 메뉴와 해당 매출을 출력
# - 아무것도 주문하지 않은 경우 빈 줄 출력됨
for menu_name in sorted(sales_menu.keys()):
    print(f"{menu_name}: {sales_menu[menu_name]}원")