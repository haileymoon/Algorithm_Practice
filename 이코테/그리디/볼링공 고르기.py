## 1번. 내 풀이
## 이중 반복문을 돌면서 모든 경우의 수를 따지고, 데이터를 비교하고 서로 다를 때만 카운트
# import sys
# n, m = map(int, sys.stdin.readline().split())
# list = list(map(int, sys.stdin.readline().split()))
# result = []
# count = 0
# for i in range(n):
#     for j in range(i, n):
#         if list[i] != list[j]:
#             result.append((i+1,j+1))
#             count += 1
# print(len(result))

# 2번. 책 풀이
# 문제를 효과적으로 해결하기 위해서는, 먼저 무게마다 볼링공이 몇 개 있는지를 계산해야한다
# 예) 무게가 1인 볼링공 : 1개, 무게가 2인 볼링공 : 1개, 무게가 3인 볼링공 : 2개
# A가 무게 1을 선택할 때 B가 선택할 수 있는 경우의 수는 3, A가 2를하면 B의 경우의 수는 2, A가 3을 하면 B의 경우의 수는 0
# 경우의 수: (A가 고른 동일한 무게를 제외하고, A가 고른 무게보다 큰 것-> 조합인데 작은 것도 포함하면 중복되니까)

import sys
n, m = map(int, sys.stdin.readline().split())
list = list(map(int, sys.stdin.readline().split()))
array = [0] * 10 #m의 최대수는 10

for data in list:
    #array는 무개 기준
    array[data] +=1

result =0

for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

## 3번 (1번 번형)
#from itertools import combinations
#
## n : 공의 개수 m : 공의 최대무게
#n, m = map(int, input().split())
#list = list(map(int, input().split()))
#
#count = 0
#for case in combinations(range(n), 2):
#    i, j = case[0], case[1]
#    if list[i] != list[j] :
#        count += 1
#print(count)