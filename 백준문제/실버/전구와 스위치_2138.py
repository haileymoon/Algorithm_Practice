import copy
length = int(input())
now = list(map(int, str(input())))
now2 = copy.deepcopy(now)
goal = list(map(int, str(input())))
count1 = 0
count2 = 0
def change(array, i):
    move = [-1,0,1]
    for step in move:
        idx = i+step
        if idx >= 0 and idx < length:
            if array[idx] == 0:
                array[idx] = 1
            else:
                array[idx] = 0

for i in range(1, length):
    if now[i-1] != goal[i-1]:
        change(now, i)
        count1 += 1
if now[-1] == goal[-1]:
    print(count1)
    exit()

count2 += 1
change(now2, 0)
for i in range(1, length):
    if now2[i-1] != goal[i-1]:
        change(now2, i)
        count2 += 1
if now2[-1] == goal[-1]:
    print(count2)
    exit()
print(-1)


# bfs로 풀려다가 append할때의 조건을 찾지 못함 -> 결과적으로 계속 append되서 무한 반복
# 찾아보니 이 문제는 그리디였음
# from collections import deque

# def change(item):
#     if item == 0:
#         return 1
#     else:
#         return 0

# move = [-1, 0, 1]

# def bfs(lights, lights_goal):
#     queue = deque()
#     queue.append((lights, 0))
#     while queue:
#         lights, depth = queue.popleft()
#         for sign in move:
#             idx = sign + depth
#             if idx >=0 and idx <len(lights):
#                 lights[idx] = change(lights[idx])
#         if lights == lights_goal:
#             return depth + 1
#         queue.append((lights, depth+1))
#         print(queue)
#     return -1
# num = int(input())
# lights_now = list(map(int, str(input())))
# lights_goal = list(map(int, str(input())))
# print(bfs(lights_now, lights_goal))
