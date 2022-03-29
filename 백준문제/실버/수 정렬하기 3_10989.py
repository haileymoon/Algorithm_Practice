import sys
import bisect
n = int(sys.stdin.readline())
# 주어지는 수의 범위 10,000

result = [0] * 10001 # 0번째 인덱스는 버리고

for _ in range(n):
    result[int(sys.stdin.readline())] += 1

for i in range(10001):
    if result[i] != 0:
        for _ in range(result[i]):
            print(i)