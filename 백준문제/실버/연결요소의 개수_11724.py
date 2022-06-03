from collections import deque
import sys
input = sys.stdin.readline
def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        visited[node] = True
        for n in node_list[node]:
            if not visited[n]:
                queue.append(n)
                visited[n] = True
n, m = map(int, input().split())
node_list = [[] for _ in range(n+1)]
count = 0
visited = [False for _ in range(n+1)]
visited[0] = True
for _ in range(m):
    a,b = map(int, input().split())
    node_list[a].append(b)
    node_list[b].append(a)
for i in range(n+1):
    if not visited[i]:
        bfs(i)
        count += 1
print(count)
