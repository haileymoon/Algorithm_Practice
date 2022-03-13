# wow this is legend 나 아까 왤케 어렵게 풀었냐;;
# 패턴을 잘 보면 올라갈때랑 내려갈때만 횟수가 추가 된다는 걸 알수있음. 좌우로 움직일때는 횟수가 그대로임
# bfs할 필요도 없음
n = int(input())
target = int(input())
value = 1
start = n//2
graph = [[-1]*n for _ in range(n)]
limit = 1
x,y= start, start
graph[x][y] = 1
while True:
    # 한 방향에서 해당 길이 만큼 움직인다, 움직이고 turn하는데, 좌우로 turn할때는 횟수가 늘어나지 않는다.
    # 함정은 위방향을 향했을때 limit이 1이 되기 위해 좌부터 for문을 시작한다.
    for _ in range(limit):
        # 위로
        value = graph[x][y]
        # 올라갔을때만 break 체크하면 됨
        x -= 1
        y += 0
        graph[x][y] = value + 1
        if x == 0 and y == 0:
             break
    if x == 0 and y == 0:
        break
    # if value-1 == n*n:
    #     break

    for _ in range(limit):
        # 오른쪽
        value = graph[x][y]
        x += 0
        y += 1
        graph[x][y] = value + 1
    limit += 1

    for _ in range(limit):
        #아래
        value = graph[x][y]
        x += 1
        y += 0
        graph[x][y] = value + 1

    for _ in range(limit):
        # 왼쪽
        value = graph[x][y]
        x += 0
        y -= 1
        graph[x][y] = value + 1
    limit += 1

answer = []
for i in range(n):
    for j in range(n):
        print(graph[i][j], end = " ")
        if graph[i][j] == target:
            answer.append(i+1)
            answer.append(j+1)
    print()
for pos in answer:
    print(pos, end = " ")




