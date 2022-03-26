# 에라토스테네스의 채
# 배수는 다 지운다
n = int(input())
count = 0
numbers = list(map(int, input().split()))
visited = [i for i in range(max(numbers)+1)]

for i in range(2, max(numbers)):
    flag = False
    idx = 2
    if visited[i] != 0:
        while idx*i <= max(numbers):
            if visited[idx*i] != 0:
                visited[idx*i] = 0
            idx += 1
if 1 in visited:
    visited.remove(1)
prime = set()
for num in numbers:
    if num in visited:
        prime.add(num)
print(len(prime))