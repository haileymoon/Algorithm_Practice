# 탈출구, 최단거리를 찾는거니까 최대한 깊이 방문해서 찾아보는 것이 아닌, 최대한 가까운 노드들부터 확인
# bfs는 queue
from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

#이동할 네가지 방향 정의
dx = [-1,+1,0,0]
dy = [0,0,-1,+1]

def bfs(x, y):
    queue = deque()
    queue.append(x,y)
    while queue: # 큐가 빌때까지 반복
        x, y = queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx >= n or ny >=m:
                continue
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단거리기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1 #이전값들의 값에다가 +1한후에 새로 찾은 곳에 값 입력
                queue.append((nx,ny))
        return graph[n-1][m-1]
print(bfs(0,0))
