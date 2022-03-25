from collections import deque

computer_count = int(input())
pairs_count = int(input())
count = 0
visited = [False for _ in range(computer_count+1)]
dictionary = {}
# 아래와 같이 하면 0부터 기록되는데 그럴 필요가 없쥬
# for i in range(computer_count+1):
#     dictionary[i] = set()

for i in range(1, computer_count+1):
    dictionary[i] = set()

for _ in range(pairs_count):
    a, b = map(int, input().split())
    dictionary[a].add(b)
    dictionary[b].add(a)


def bfs(start):
    global dictionary
    global count

    queue = deque([start])

    while queue:
        num = queue.pop()
        for i in dictionary[num]:
            if not visited[i]:
                visited[i] = True
                count += 1
                queue.append(i)


bfs(1)
# 1번 컴퓨터는 빼줌
print(count-1)