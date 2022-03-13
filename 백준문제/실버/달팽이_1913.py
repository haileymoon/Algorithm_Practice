from collections import deque

n = int(input())
target = int(input())
graph = [[-1] * n for i in range(n)]
start = n//2
graph[start][start] = 1
queue = deque()
queue.append((start, start))
turn = -1
count = 0
value = 1
line_length = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
target_pos = []

# 같은 개수로 두 번씩 진행됨. 한칸 두번, 두칸 두번, 세칸 두번, 네칸 두번
# turn은 매번 달라지지만 count는 두번 마다 바뀜
while queue:
    x,y = queue.popleft()
    if -1 < x < n and -1 < y < n:
        turn += 1
        if turn == 4:
            turn = 0
        next_x = x
        next_y = y
    else: continue

    #범위 체크
    for _ in range(2):
        while line_length > count:
            next_x += dx[turn]
            next_y += dy[turn]
            if -1 < next_x < n and -1 < next_y < n:
                if graph[next_x][next_y] == -1:
                    graph[next_x][next_y] = value + 1
                    value = graph[next_x][next_y]
                    count += 1

            else:
                break
        turn += 1
        if turn == 4:
            turn = 0
        count = 0
    line_length += 1
    queue.append((next_x, next_y))
    turn -= 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end = " ")
        if graph[i][j] == target:
            target_pos.append(i+1)
            target_pos.append(j+1)
    print()
for pos in target_pos:
    print(pos, end = " ")