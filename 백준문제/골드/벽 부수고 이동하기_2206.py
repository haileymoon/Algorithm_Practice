# 그래프를 손상시키지않으며 경우의 수를 확인해야한다는 느낌이 들었는데 어떻게 해결할지 아이디어가 생각이 잘 나지않아 
# 블로그를 찾아보니 모두 visited 배열을 3차원으로 접근하시더라. 뚫지 않은 애와 뚫은 애의 정보를 한번에 다 담아버리는 것, 
# 또 그래프를 훼손시키지않고 visited에 결과를 담아 관리한다. bfs중에서도 visited 3차원 배열은 좀 생소했다.

from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
n, m = map(int, input().split())
graph = []
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(start):
    queue = deque()
    # ((x,y), wall_break)
    queue.append((start, 0))
    visited[0][0][0] = 1
    
    while queue:
        location, wall_break = queue.popleft()
        x, y = location
        if x == n-1 and y == m-1:
            return visited[x][y][wall_break]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위내에 있고 방문하지 않았다면,
            if 0<= nx < n and 0<= ny < m and visited[nx][ny][wall_break] == 0:
                #graph의 형태는 유지하는데 visited에 기록
                if graph[nx][ny] == 0:
                    visited[nx][ny][wall_break] = visited[x][y][wall_break] + 1
                    queue.append(((nx,ny), wall_break))
                #벽에 아직 부딫히지 않은 애가 벽을 마주했을때
                if graph[nx][ny] == 1 and wall_break == 0:
                    visited[nx][ny][1] = visited[x][y][wall_break] + 1
                    queue.append(((nx,ny), 1))
    #마지막까지 닿지 못했을 때
        print(visited)
    return -1

print(bfs((0,0)))

# 수정 전 코드: 벽을 뚫었는지 못뚫었는지 확인하는 값을 넘겨주며 체크했다. 예시는 다 통과했지만 반례중에서 벽을 뚫지 않아도 되는 구간에서 뚫고 나중에는 막혀버려서 도달하지 못하는 예시가 있었다. 아래는 수정 전 코드이다
# from collections import deque
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# n, m = map(int, input().split())
# graph = []
# visited = [[False]*m for _ in range(n)]

# for _ in range(n):
#     graph.append(list(map(int, input())))

# def bfs(start):
#     queue = deque()
#     # ((x,y), wall_break)
#     queue.append((start, False))
#     while queue:
#         location, wall_break = queue.popleft()
#         x, y = location
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx <0 or ny < 0 or nx>=n or ny >=m:
#                 continue
#             if graph[nx][ny] == 0:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append(((nx,ny), wall_break))
#             elif graph[nx][ny] == 1:
#                 # 벽을 한개 이상 마주치면 멈춤
#                 if wall_break:
#                     continue
#                 # 벽을 처음 마주쳤을 때 
#                 else:
#                     graph[nx][ny] = graph[x][y] + 1
#                     queue.append(((nx,ny), True))
#         print(queue)
#         print(graph)
#     #마지막까지 닿지 못했을 때
#     if graph[n-1][m-1] == 0:
#         return -1
#     else:
#         #graph의 마지막
#         return graph[n-1][m-1]

# graph[0][0] = 1
# print(bfs((0,0)))
