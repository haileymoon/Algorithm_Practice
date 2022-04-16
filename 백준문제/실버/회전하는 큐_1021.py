from collections import deque
num, n = map(int, input().split())
selected = list(map(int, input().split()))
numbers = deque([i for i in range(1, num+1)])
answer = 0

for s in selected:
    if numbers[0] == s:
        numbers.popleft()
        continue
    else:
        if numbers.index(s) < len(numbers)/2:
            while numbers[0] != s:
                numbers.rotate(-1)
                answer += 1
        else:
            while numbers[0] != s:
                numbers.rotate(1)
                answer += 1
    if numbers[0] == s:
        numbers.popleft()

print(answer)