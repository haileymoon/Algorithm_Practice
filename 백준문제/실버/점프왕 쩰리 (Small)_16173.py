import sys
# bfs 로 해결해볼 것
from collections import deque

n = int(sys.stdin.readline())
graph = []
visited = [[False]*n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

#이기는 방법이 있을시에만 True로 바꿔줌
flag = False

queue = deque()
#첫 시작은 맨왼쪽 맨 위니까 첫번째 위치 넣어줌
queue.append((0,0))
while queue:
    x,y = queue.pop()
    visited[x][y] = True
    skip = graph[x][y]
    if skip == -1:
        print("HaruHaru")
        flag = True
        break
    #오른쪽
    dy = 1
    dy *= skip
    if y + dy <= n - 1 and visited[x][y + dy] != True:
        queue.append((x, y+dy))
    # 범위를 벗어나면 queue에 넣지 않음

    #아래쪽
    dx = 1
    dx *= skip
    if x + dx <= n - 1 and visited[x + dx][y] != True:
        queue.append((x+dx, y))
    # 범위를 벗어나면 queue에 넣지 않

if flag == False:
    print("Hing")
