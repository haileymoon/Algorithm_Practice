# 모든 모서리를 방문처리 자신의 위치와 1까지의 차이만큼 더해줌
# 도는 사이클을 보면 n-1만큼 돈다, 그리고 기본적으로 첫번째 사이클엔 3번 turn한다

m, n = map(int, input().split())
if m>n:
    print(2*(n-1)+1)
    if n%2 ==0:
        print(int((n/2)+1), int(n/2))
    else:
        print(int((n+1)/2+(m-n)), int((n+1)/2))
elif m<=n:
    print(2*(m-1))
    if m == n:
        if m%2 == 0:
            print(int((m/2)+1), int(m/2))
        else:
            print(int((m+1)/2), int((m+1)/2))
    else:
        if m%2 == 0:
            print(int((m/2)+1), int(m/2))
        else:
            print(int((m+1)/2), int(((m+1)/2)+(n-m)))


# 아래는 메모리 초과를 벗어나기 위해 바꿨는데 시간초과
# m, n = map(int, input().split())
# count = 0
# turn_count = 0
#
# x = 0
# y = 0
# x_left_limit = n-1
# x_right_limit = 0
# y_down_limit = m-1
# y_up_limit = 1 # 함정주의!! 첫번째 turn에 y=0했으니 1이 limit이여야
#
# while True:
#     if count == 4:
#         count = 0
#
#     if count == 0: #방향 우
#         x += 1
#         if x_left_limit == x_right_limit:
#             count+=1
#             continue
#         while x != x_left_limit:
#             x += 1
#         x_left_limit = x-1
#         turn_count += 1
#         count += 1
#     elif count == 1 : #방향 아래
#         y+=1
#         if y_up_limit == y_down_limit:
#             count+=1
#             continue
#         while y != y_down_limit:
#             y += 1
#         y_down_limit = y-1
#         turn_count += 1
#         count += 1
#     elif count == 2: #좌 방향
#         x -= 1
#         if x_left_limit == x_right_limit:
#             count +=1
#             continue
#         while x != x_right_limit:
#             x -= 1
#         x_right_limit = x+1
#         turn_count += 1
#         count+=1
#     else: #위 방향
#         y -= 1
#         if y_up_limit == y_down_limit:
#             count+=1
#             continue
#         while y != y_up_limit:
#             y -= 1
#         y_up_limit = y+1
#         turn_count += 1
#         count += 1
#     # 끝을 마주했을때의 조건문
#     if x_left_limit==x_right_limit and y_up_limit == y_down_limit:
#         break
# print(turn_count)
# print(y+1,x+1)

# 아래는 메모리 초과

# while True:
#      if idx == 4:
#          idx = 0
#      x += dx[idx]
#      y += dy[idx]
#      if -1 < x < m and -1 < y < n:
#          if graph[x][y] == 0: # 방문하지않았다면
#              graph[x][y] = 1 # 방문처리
#              count -= 1
#          else:
#              x -= dx[idx]
#              y -= dy[idx]
#              idx += 1
#              turn_count +=1
#      else:
#          x -= dx[idx]
#          y -= dy[idx]
#          idx += 1
#          turn_count += 1
#
#      if count == 0:
#          break
#  print(turn_count)
#  print(x+1,y+1)
#

# m, n = map(int, input().split())
# count = n*m-1 #총 실행할 횟수, -1: 첫번째꺼는 방문처리했으니
# turn_count = 0
#
# start = [0,0]
# x, y = map(int, start)
# graph = [[0] * n for _ in range(m)]
# graph[x][y] = 1
#
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# idx = 0


# while True:
#     if idx == 4:
#         idx = 0
#     x += dx[idx]
#     y += dy[idx]
#     if -1 < x < m and -1 < y < n:
#         if graph[x][y] == 0: # 방문하지않았다면
#             graph[x][y] = 1 # 방문처리
#             count -= 1
#         else:
#             x -= dx[idx]
#             y -= dy[idx]
#             idx += 1
#             turn_count +=1
#     else:
#         x -= dx[idx]
#         y -= dy[idx]
#         idx += 1
#         turn_count += 1
#
#     if count == 0:
#         break
# print(turn_count)
# print(x+1,y+1)