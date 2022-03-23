# 세로, 가로
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
possible_num = []

def count_recolor(i,j):
    #w로 바꿔야 하는 수
    w_count = 0
    #b로 바꿔야 하는 수
    b_count = 0
    for k in range(i, i+8):
        for l in range(j, j+8):
            if (k+l) % 2:
                if graph[k][l] == "W":
                    #black이 스타트라면
                    b_count += 1
                else:
                    #white가 스타트라면
                    w_count += 1
            else:
            #홀수일 때
                if graph[k][l] == "W":
                    #white가 스타트라면
                    w_count += 1
                else:
                    #black이 스타트라면
                    b_count += 1

    possible_num.append(w_count)
    possible_num.append(b_count)




for i in range(n-8+1):
    for j in range(m - 8 + 1):
        count_recolor(i,j)
print(min(possible_num))
