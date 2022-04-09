import sys
n, m = map(int, sys.stdin.readline().split())
s = set(sys.stdin.readline().rstrip() for _ in range(n))
count = 0
for _ in range(m):
    check = sys.stdin.readline().rstrip()
    if check in s:
        count += 1
print(count)