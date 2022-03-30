import sys
from collections import deque

case = int(sys.stdin.readline())
queue = deque()
# 위 아래 좌 우
def bfs(queue, graph):
    count = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        x, y = queue.pop()
        if graph[y][x] == 1:
            count += 1
            graph[y][x] = 0
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx > m-1 or 0 > ny or ny > n-1:
                continue
            else:
                if graph[ny][nx] == 0:
                    continue
                else:
                    queue.append((nx, ny))
                    graph[ny][nx] = 0
    return count


for _ in range(case):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0]* m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
        queue.append((x, y))

    print(bfs(queue, graph))