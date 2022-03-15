n = int(input())
current = list(map(int, input().split()))
m = max(current)
# 모든 점수를 점수/M*100으로
for i, score in enumerate(current):
    current[i] = score/m*100
print(sum(current)/len(current))