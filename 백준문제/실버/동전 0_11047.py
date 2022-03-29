n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
count = 0
for coin in coins[::-1]:
    count += k // coin
    k %= coin
    if k == 0:
        break
print(count)