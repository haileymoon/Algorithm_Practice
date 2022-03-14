row, column = map(int, input().split())
graph = [[-1]*column for _ in range(row)]
x = 0
y = 0
graph[x][y] = 0
count = 0
answer = 1

dx = [0,1,0,-1] #오른쪽, 아래, 왼쪽, 위
dy = [1,0,-1,0]
idx = 0
while True:
    if idx == 4:
        idx = 0

    if x+dx[idx]<0 or x+dx[idx]>=row:
        count += 1
        idx += 1
        continue
    elif y+dy[idx]<0 or y+dy[idx]>=column:
        count += 1
        idx += 1
        continue
    elif graph[x+dx[idx]][y+dy[idx]] == 0:
            count += 1
            idx +=1
            continue
    else:
        x += dx[idx]
        y += dy[idx]
        graph[x][y] = 0
        answer+=1
    if answer == row*column:
        break
    print(graph)
print(count)