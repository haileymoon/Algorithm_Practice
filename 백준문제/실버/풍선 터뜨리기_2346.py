n = int(input())
balloons = list(map(int, input().split()))
visited = [False for _ in range(len(balloons))]
answer = [1]
visited[0] = True
move = balloons[0]
idx =0

while len(answer) <n:
    count = 0

    while count < abs(move):
        if move < 0:
            idx = (idx - 1) % n
        else:
            idx = (idx + 1) % n

        if visited[idx]:
            continue
        else:
            count += 1

    answer.append(idx + 1)
    move = balloons[idx]
    visited[idx] = True


print(*answer)

