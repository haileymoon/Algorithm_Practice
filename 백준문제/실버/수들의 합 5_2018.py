from collections import deque

n = int(input())
count = 1
stack = deque()
value = 0

for i in range(1,n+1):
    stack.append(i)
    value = sum(stack)
    if value == n:
        count += 1
        stack.popleft()
    if value < n:
        continue
    if value >= n:
        while sum(stack) >= n:
            stack.popleft()
            if sum(stack) == n:
                count +=1
    #바로 옆과 더했을때 n보다 크면 더이상 더하는 것이 의미없음
    if i+i+1 > n or stack == 0:
        break
print(count)