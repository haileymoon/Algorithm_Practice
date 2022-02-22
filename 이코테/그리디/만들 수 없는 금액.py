# N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값
# 나올 수 있는 수의 max는 (a+b+c)+1

# 내가 처음에 생각한 것: 같은 화폐 (1,1,3)이 들어왔을 때 원소들을 각각 더했을때의 경우의 수 구할때
# 비효율적일 것 같다 생각했다 같은 1인데 인덱스가 다르니까 3+1이 두번 이루어지기 때문
# 하지만 방법이 딱히 생각이 나지 않아 비효율적이더라도 모든 경우의 합을 구하고, 1~ 돌며 빠져있는 첫번째 수
# 또는 빠져있는 수가 없을 땐 전체 원소의 합+1(이룰 수 있는 최대의 수)로 마무리

# 1: 내풀이
# import sys
# N = int(sys.stdin.readline())
# coins = list(map(int, sys.stdin.readline().split()))
# answer = []
# result = -1
#
# for i in range(N):
#     for j in range(i+1,N+1):
#         answer.append(sum(coins[i:j])) #j인덱스 전까지 포함해서 잘라서 N+1으로 처리 -> 모든 경우의 수 계산
# for i in range(1, len(answer)):
#     if i in answer:
#         continue
#     else:
#         result = i
#         break
# if result == -1:
#     result = sum(coins[0:N+1])+1
# print(result)

# 2
# 찾아보니 비슷하게 조합(combination)을 사용한 코드가 있더라: but 시간 부담 똑같이 high
# from itertools import combinations
# n = int(input())
# coins = list(map(int, input().split()))
# result =[]
# answer = 0
#
# for i in range(1,n+1):
#     combi_list = list(combinations(coins,i)) # sum은 각 tuple마다 값 계산 가능
#     for tuple in combi_list:
#         result.append(sum(tuple))
# for i in range(1,len(result)+1):
#     if i in result:
#         continue
#     else:
#         answer = i
#         break
# if answer ==0:
#     answer = sum(coins)+1
#
# print(answer)

# 책 풀이: 화폐가 작은 순서대로 동전을 확인하며 현재 확인하는 동전을 이용해 특정 금액(target)을 만들 수 있는지 확인
# 만약 target금액을 만들 수 있다면, target값 업데이트
# 만들 수 있는지 없는지 판단하는 금액 >= 확인하고 있는 화폐 단위면 break.
import sys
N = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))
coins.sort()
target = 1

for coin in coins:
    if target<coin:
        break
    target += coin

print(target)

