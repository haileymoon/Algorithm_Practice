# 전과 현재만 다르면된다는 아이디어로 아래와 같은 코드를 짯는데 테스트케이스 중 하나가 걸렸다. 자세히 보니 난 그리디 형식으로 최소만 찾아 한 방향으로만 답을 찾았는데
# 1 2 3
# 6 5 9
# 9 1 9
# 이럴때 나의 방식으로 가면 1->5->9가 된다.
# 최소를 구하려면 1->6->1이 되어야 한다.
# 그래서 모든 경우의 수를 확인하며 값을 구하려고 bfs를 적용할까 했는데, 그러면 문제에서 요구하는 0.5초 이상이 걸릴 것 같았다.
# 따라서 구글링을 통해서 이후의 것을 찾는게 아니라 각 번호마다 이전의 선택을 했을 때의 결과를 가지도록하여 경우의 수를 커버한다는것을 알 수 있었다.
n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
for i in range(1, len(p)):
    #빨강
    p[i][0] = min(p[i-1][1],p[i-1][2]) + p[i][0] 
    #초록
    p[i][1] = min(p[i-1][0],p[i-1][2]) + p[i][1] 
    #파랑
    p[i][2] = min(p[i-1][0],p[i-1][1]) + p[i][2] 
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))

# import sys
# input = sys.stdin.readline
# num = int(input())
# sum = 0
# prev = -1
# for _ in range(num):
#     house = list(map(int, input().split()))
#     if prev == -1:
#         min_num = min(house)
#         sum = min_num
#         prev = house.index(min_num)
#     else:
#         house[prev] = 1001
#         min_num = min(house)
#         sum += min_num
#         prev = house.index(min_num)
#     print(sum, min_num)
# print(sum)
