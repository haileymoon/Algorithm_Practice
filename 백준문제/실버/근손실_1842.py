#1. DFS(재귀) 풀이
n, k = map(int, input().split())
work_out = list(map(int, input().split()))
visited = [False for _ in range(n)]
count= 0
def dfs(depth, weight):
    global count
    if depth == n:
        count += 1
        return
    for i in range(n):
        next_weight = weight + work_out[i] - k
        if next_weight >= 500 and not visited[i]:
            visited[i] = True
            dfs(depth + 1, next_weight)
            visited[i] = False
    
dfs(0,500)     
print(count)

# #2. permutations 풀이
# from itertools import permutations
# n, k = map(int, input().split())
# work_out = list(map(int, input().split()))
# count = 0
# for set in permutations(work_out,n):
#     total = 500
#     flag = False
#     for j in set:
#         if total - k + j  < 500:
#            flag = True
#            break
#         else:
#             total = total - k + j
#     if not flag:
#         count += 1
# print(count)
