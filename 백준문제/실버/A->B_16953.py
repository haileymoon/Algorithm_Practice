#구현으로 푼 방법
start, target = input().split()
count = 0
while int(target) > int(start):
    if target[-1] == "1":
        target = target[:-1]
        count +=1
    elif int(target)%2 == 0:
        target = str(int(target) // 2)
        count +=1
    else:
        count = -1
        break
 
if count != -1 and start == target:
    print(count+1)
elif count != -1:
    print(-1)
else:
    print(-1)
    
#bfs로 푼 방법
from collections import deque
a, b = map(int, input().split())
# key: 숫자, value: 연산횟수
visited = dict()
visited[a] = 1
def bfs(start):
    queue = deque([start])
    while queue:
        num = queue.popleft()
        if num == b:
            return visited[num]
        move = [num*2, int(str(num)+"1")]
        for new_num in move:
            if new_num not in visited.keys() and new_num <= 10**9:
                visited[new_num] = visited[num] + 1
                queue.append(new_num)
    return -1

print(bfs(a))
