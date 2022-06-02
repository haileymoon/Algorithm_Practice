#1. permutations 풀이
from itertools import permutations
n, k = map(int, input().split())
work_out = list(map(int, input().split()))
count = 0
for set in permutations(work_out,n):
    total = 500
    flag = False
    for j in set:
        if total - k + j  < 500:
           flag = True
           break
        else:
            total = total - k + j
    if not flag:
        count += 1
print(count)
