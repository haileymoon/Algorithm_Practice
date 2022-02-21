# N*M개수의 카드가 주어졌을 때 N(행)을 먼저 선택한 다음, 그 행에서 가장 작은 수를 뽑아줌
# 근데 뽑은 그 숫자가 최대한 높게 출력되어야 함
import sys
n, m = map(int, sys.stdin.readline().split())
data = 0
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    if min(row) > data: # 유사 방법: data = max(data, min(row)) -> 큰 수 찾기
        data = min(row)
print(data)