import copy
import sys
from collections import deque
n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

distance = [-1] * (n + 1)
distance[x] = 0  # 시작 도시 가는 거리 0

for i in range(m):
    a, b = (map(int, sys.stdin.readline().split()))
    graph[a].append(b)

queue = deque()
queue.append(x)
def bfs(x):
    while queue:
        now = queue.popleft()
        for line in graph[now]:
            if distance[line] == -1:
                distance[line] = distance[now] + 1
                queue.append(line)
bfs(x)

check = False
for i, connected in enumerate(distance):
    if connected == k:
        print(i)
        check = True
if check == False:
    print(-1)

# #책에 있는 첫번째 예외케이스를 못잡아냄 ㅜ
# def bfs(x):
#     result = []
#     count = x
#     while queue:
#          copy_list = copy.deepcopy(lists)
#          num = queue.popleft()
#          for i, line in enumerate(lists):
#              if line[0] == num:
#                  queue.append(line[1])
#                  # 만약 이미 어떤 도시를 지나갔으면 빼줘야하는데 result안의 tuple의 1번째를 확인해야함...
#                  result.append((copy_list[i][1], (count+1)-x))
#                  copy_list[i][1] = count+1
#              else: continue
#          count += 1
# #
#     return result
# result = bfs(x)
# answer = []
# for tuple in result:
#      if tuple[1] == k:
#          answer.append(tuple[0])
# answer.sort()
# if answer:
#     for a in answer:
#          print(a)
# else:
#     print(-1)