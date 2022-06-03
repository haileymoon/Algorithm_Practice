n, m = map(int, input().split())
graph_now = []
graph_goal = []
count = 0
def change(graph, i, j):
    for x in range(3):
        for y in range(3):
            if graph[i+x][j+y] == 0:
                graph[i+x][j+y] = 1
            else:
                graph[i+x][j+y] = 0
            
for _ in range(n):
    graph_now.append(list(map(int, str(input()))))
for _ in range(n):
    graph_goal.append(list(map(int, str(input()))))

for i in range(n):
    for j in range(m):
        #하나가 잘못되면 즉시 그 잘못된 부분을 시작으로 3*3 change
        #만약 바꿀 수 없는데 잘못되면 print(-1)
        if i >= n-2 or j >= m-2:
            if graph_now[i][j] != graph_goal[i][j]:
                print(-1)
                exit()
        if graph_now[i][j] != graph_goal[i][j]:
            change(graph_now, i, j)
            count += 1
print(count)
