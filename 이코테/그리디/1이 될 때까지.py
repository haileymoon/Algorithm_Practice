n, k = map(int, input().split())
count = 0

while True:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1
    if n == 1:
        break
# 빼야하는 수를 구하려면
# target = (n//k) * k 하고 n-target하면 나눌 수 없는 숫자만 나오게 됨. -> -1을 해줘야 하는 아이들
print(count)