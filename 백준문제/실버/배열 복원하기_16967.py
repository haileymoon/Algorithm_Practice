H, W, X, Y = map(int, input().split())
b = []
answer = []
# for _ in range(H+X):
#     b.append(list(map(int, input().split())))
# for sub in b:
#     if sub[0] == 0:
#         if sub[Y:] not in answer:
#             answer.append(sub[Y:])
#     elif sub[-1] == 0:
#         if sub[:-Y] not in answer:
#             answer.append(sub[:-Y])


for ans in answer:
    print(*ans)
for _ in range(H+X):
    b.append(list(input().split()))

answer = [[] for _ in range(H)]
for i in range(X):
    answer[i] = list(map(int, b[i][:W]))

for i in range(X, H):
    for j in range(W):
        if j < Y:
            answer[i].append(int(b[i][j]))
        else:
            inner = j - Y
            answer[i].append(int(b[i][j]) - int(answer[i-X][j-Y]))

for ans in answer:
    print(*ans)