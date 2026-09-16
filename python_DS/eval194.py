# 각 줄을 `split(",")` 후 int 로 변환, 소계 누적.
n = int(input())

# 총액을 구하기 위한 변수 
total = 0

# 입력받은 값 반복하며 만큼 품목, 개수, 단가를 입력받는다
for _ in range(n):

    # ","를 기준으로 세 개의 변수에 나눠서 입력받은 후, 개수와 단가를 정수로 변환
    merch, qty, unit_price = input().split(",")
    qty = int(qty)
    unit_price = int(unit_price)

    # (수량 * 단가)를 별도의 변수에 저장
    # - 총액 변수에 더함
    subtotal = qty * unit_price
    total += subtotal

    # 품목별 수량과 가격을 각각 출력 
    print(f"{merch} x{qty}: {subtotal}원")

# 반복문 바깥에서 총액을 출력
print(f"총액: {total}원")