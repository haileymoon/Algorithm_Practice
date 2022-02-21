# 손님한테 거슬러 줄 수 있는 동전의 최소개수
# 거슬러 줘야할 돈이 N이고 10의 배수이다.
# 동전은 500,100,50,10원이 무한히 있음

# 핵심 아이디어-> 가장 큰 화폐단위부터 지급
N = 1260
coins = [500, 100, 50, 10]
count = 0
for coin in coins:
    count += N // coin
    N %= coin
    if N == 0:
        break
print(count)